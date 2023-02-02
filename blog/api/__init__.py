from flask_restful import Api

from blog.api.tag import TagList

current_api = None


def ini_app(app):
    api = Api(app)
    current_api = api
    api.add_resource(TagList, "/api/tags/")
    return api


__all__ = ["current_api"]
