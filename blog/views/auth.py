from re import error

from flask import Blueprint, current_app, redirect, render_template, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_wtf.csrf import logging
from jinja2 import is_undefined
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from blog.forms.user import LoginForm, RegistrationForm
from blog.models.database import db
from blog.models.user import UserModel

auth_app = Blueprint("auth_app", __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            return render_template(
                "auth/login.html", form=form, error="User(username) not exist"
            )
        if not user.password_vildate(form.password.data):
            return render_template(
                "auth/login.html", form=form, error="Invalid username or password"
            )
        login_user(user)
        return redirect(url_for("index"))
    return render_template("auth/login.html", form=form)


@auth_app.route("/login_as/", methods=["GET", "POST"], endpoint="login_as")
def login_as():
    if not (current_user.is_authenticated and current_user.is_staff):
        raise NotFound


@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@auth_app.route("/register/", methods=["GET", "POST"], endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    error = None
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        if UserModel.query.filter_by(username=form.username.data).count():
            form.username.errors.append("User allready exist")
            return render_template("auth/register.html", form=form)
        if UserModel.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email allready exist")
            return render_template("auth/register.html", form=form)
        user = UserModel(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            is_staff=False,
        )
        user.password = form.password.data
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception(error)
            logging.error(error)
        else:
            current_app.logger.info("Created user %s", user)
            login_user(user)
            return redirect(url_for("index"))
    return render_template("auth/register.html", form=form, error=error)


@auth_app.route("/secret/", endpoint="secret")
@login_required
def secret_view():
    if current_user.is_staff:
        return "Super secret data"
    else:
        return redirect("/")


__all__ = [
    "login_manager",
    "auth_app",
]
