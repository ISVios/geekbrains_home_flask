from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource
from webargs import fields

from blog.models import TagModel, db, tag
from blog.schema import TagSchema


@marshal_with(TagSchema(many=True))
class TagList(MethodResource):
    def get(self):
        tags = TagModel.query.all()
        return tags


@marshal_with(TagSchema)
class TagDetail(MethodResource):
    @use_kwargs({"tag_id": fields.Integer()}, location="query")
    def get(self, tag_id=0):
        return TagModel.query.filter(TagModel.id == tag_id).one()
