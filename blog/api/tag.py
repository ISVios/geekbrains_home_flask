import logging
from flask_restful import Resource
from blog.schema import TagSchema
from blog.models import db, TagModel, tag


class TagList(Resource):
    def get(self):
        tags = TagModel.query.all()
        ser = TagSchema().dump(tags, many=True)
        return ser


class TagDetail(Resource):
    def get(self, id):
        tag = TagModel.query.get(id)
        if tag:
            return TagSchema().dump(tag)
        else:
            return {}
