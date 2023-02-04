import logging

from flask import abort, current_app, request, session
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource, MethodResourceMeta
from flask_login import current_user
from flask_restful import Resource
from webargs import fields

from blog.models import TagModel
from blog.models.database import session, db
from blog.schema import TagSchema
from blog.api.database import (
    del_method,
    get_all,
    get_by_id,
    patch_method,
    post_method,
    need_authenticated,
)
from blog.schema.tag import TagWithoutIdSchema


@doc(tags=["Tag"])
class TagList(MethodResource):
    # Todo conver to Auto class
    # class Meta:
    #     model = TagModel
    #     session = db.session
    #     schema = TagSchema(many=True)

    @marshal_with(TagSchema(many=True))
    @need_authenticated
    def get(self):
        return get_all(TagModel)


@doc(tags=["Tag"])
class TagDetail(MethodResource):
    @marshal_with(TagSchema)
    @use_kwargs(TagWithoutIdSchema)
    @need_authenticated
    def post(self, **kwargs):
        return post_method(TagModel, session, **kwargs)

    @marshal_with(TagSchema)
    @need_authenticated
    def get(self, id):
        return get_by_id(TagModel, id)

    @need_authenticated
    def delete(self, id):
        return del_method(TagModel, session, id)

    @use_kwargs(TagWithoutIdSchema)
    @marshal_with(TagSchema)
    @need_authenticated
    def patch(self, id, **kwargs):
        return patch_method(TagModel, session, id, **kwargs)
