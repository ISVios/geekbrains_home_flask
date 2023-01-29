from flask import Blueprint, render_template

from blog.models import AuthorModel

import logging

author_app = Blueprint("author_app", __name__)

@author_app.route("/", endpoint="list")
def author_list():
    authors = AuthorModel.query.all()
    return render_template("authors/list.html", authors=authors)


