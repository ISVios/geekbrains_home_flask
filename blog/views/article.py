from flask import Blueprint, render_template

ARTICLES = ["Flask", "Django", "JSON:API"]

article_app = Blueprint("article_app", __name__)


@article_app.route("/", endpoint="list")
def article_list():
    return render_template("article/list.html", articles=ARTICLES)
