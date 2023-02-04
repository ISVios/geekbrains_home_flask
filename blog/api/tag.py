import logging
from flask import request

from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource
from webargs import fields

from blog.models import TagModel, db, tag
from blog.schema import TagSchema


@doc(tags=["Tag"])
@marshal_with(TagSchema(many=True))
class TagList(MethodResource):
    def get(self):
        tags = TagModel.query.all()
        return tags, 200

    @marshal_with(TagSchema)
    @use_kwargs(TagSchema)
    def post(self, **kwargs):
        tag = TagModel(**kwargs)
        db.session.add(tag)
        db.session.commit()
        return tag, 201


@doc(tags=["Tag"])
@marshal_with(TagSchema)
class TagDetail(MethodResource):
    def get(self, id):
        return TagModel.query.filter(TagModel.id == id).one_or_none()

    @use_kwargs(TagSchema)
    def put(self, id, **kwargs):
        tag = TagModel.query.filter(TagModel.id == id).one_or_none()
        if not tag:
            tag = TagModel()
        for key, value in kwargs.items():
            setattr(tag, key, value)
        db.session.add(tag)
        db.session.commit()
        return tag, 201

    def delete(self, id):
        tag = TagModel.query.filter(TagModel.id == id).one_or_none()
        if not tag:
            return tag, 404

        db.session.delete(tag)
        db.session.commit()

        return {}, 204

    @use_kwargs(TagSchema)
    def patch(self, kwargs):
        return self.put(kwargs)
