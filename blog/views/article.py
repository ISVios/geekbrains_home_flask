import logging

from flask import Blueprint, current_app, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from blog.forms.article import CreateArticleForm
from blog.models import ArticleModel, db
from blog.models.author import AuthorModel

article_app = Blueprint("article_app", __name__)


@article_app.route("/", endpoint="list")
def article_list():
    articles = ArticleModel.query.all()
    return render_template("article/list.html", articles=articles)


@article_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id):
    article = ArticleModel.query.filter_by(id=article_id).one_or_none()
    if article is None:
        raise NotFound
    return render_template("article/detail.html", article=article)


@article_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        article = ArticleModel(title=form.title.data.strip(), body=form.body.data)
        db.session.add(article)
        if current_user.author:
            article.author = current_user.author
        else:
            current_app.logger.debug(f"{current_user} no have author model")
            author = AuthorModel(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = author
            current_app.logger.debug(f"{current_user} bind with {author}")
        try:
            db.session.commit()
            current_app.logger.debug(f"{current_user} created {article} ")
        except IntegrityError:
            error = "Counld not create a new article!"
            current_app.logger.exception(error)
        else:
            return redirect(url_for("article_app.details", article_id=article.id))
    return render_template("article/create.html", form=form, error=error)
