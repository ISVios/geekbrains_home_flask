from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import UserModel


users_app = Blueprint("users_app", __name__)


@users_app.route("/", endpoint="list")
def users_list():
    users = UserModel.query.all()
    return render_template("user/list.html", users=users)


@users_app.route("/<int:user_index>/", endpoint="detail")
def user_detail(user_index: int):
    user = UserModel.query.filter_by(id=user_index).one_or_none()
    if user is None:
        raise NotFound(f"User #{user_index} no found.")
    return render_template("user/detail.html", user=user)
