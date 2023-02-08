import logging
from operator import pos

from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_login import current_user, login_required
from flask_restful import abort
from marshmallow import Schema, fields

from blog.models import UserModel
from blog.models.database import session
from blog.schema import UserSchema
from blog.api.database import (
    del_method,
    get_all,
    get_by_id,
    patch_method,
    post_method,
    need_authenticated,
    need_authenticated_,
)
from blog.schema.user import UserWithoutIdSchema


@doc(tags=["User"])
class UserList(MethodResource):
    @marshal_with(UserSchema(many=True))
    @need_authenticated(only_staff=True)
    def get(self):
        return get_all(UserModel)


@doc(tags=["User"])
class UserDetail(MethodResource):
    @marshal_with(UserSchema)
    @use_kwargs(UserWithoutIdSchema)
    @need_authenticated()  # ToDo: <--- Think (reg in app)
    def post(self, **kwargs):
        return post_method(UserModel, session, **kwargs)

    @marshal_with(UserWithoutIdSchema)
    @need_authenticated()
    def get(self, id):
        return get_by_id(UserModel, id)

    @marshal_with(UserSchema)
    @use_kwargs(UserWithoutIdSchema)
    @need_authenticated(staff_only=True)
    def patch(self, id, **kwargs):
        # Todo add new_password and new_passwod_dup (check, set)
        return patch_method(UserModel, session, id, **kwargs)

    @need_authenticated(staff_only=True)
    def delete(self, id):
        return del_method(UserModel, session, id)
