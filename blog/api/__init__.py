import apispec
from apispec import plugin
from flask_apispec import FlaskApiSpec
from flask_restful import Api
from flask_perm import Perm

from blog.api.tag import TagDetail, TagList
from blog.api.user import UserDetail, UserList
from blog.api.article import ArticleList, ArticleDetail

current_api = None

current_doc = None


def init_doc(app):
    current_doc = None  # FlaskApiSpec(app)
    # User doc
    # current_doc.register(UserList)
    # current_doc.register(UserDetail)
    # # Tag doc
    # current_doc.register(TagList)
    # current_doc.register(TagDetail)
    # # Article Doc
    # current_doc.register(ArticleList)
    # current_doc.register(ArticleDetail)
    return current_doc


def init_app(app):
    current_api = Api(app)
    # User Api
    current_api.add_resource(UserList, "/api/users/")
    current_api.add_resource(UserDetail, "/api/users/<int:id>/")
    # Tag Api
    # current_api.add_resource(TagList, "/api/tags/")
    # current_api.add_resource(TagDetail, "/api/tags/<int:id>/")
    # Article Api
    # current_api.add_resource(ArticleList, "/api/articles/")
    # current_api.add_resource(ArticleDetail, "/api/articles/<int:id>/")
    return current_api


__all__ = ["current_api", "current_doc"]
