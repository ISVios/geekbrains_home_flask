import logging
from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource
from flask_login import login_required
from marshmallow import Schema, fields

from blog.models import UserModel
from blog.schema import UserSchema


@doc(tags=["User"])
@marshal_with(UserSchema(many=True))
class UserList(MethodResource):
    @login_required
    def get(self):

        return UserModel.query.all()

    @use_kwargs(UserSchema)
    def put(self):
        return {}


class IdScema(Schema):
    id_p = fields.Integer(as_string=True, required=True)


@doc(tags=["User"])
@marshal_with(UserSchema)
class UserDetail(MethodResource):
    @use_kwargs({"id": fields.Integer()}, location="url_field")
    @login_required
    def get(self, id):
        return UserModel.query.filter(UserModel.id == id).one()

    @use_kwargs(UserSchema, location=("json"))
    def patch(self, id):
        return {}

    def delete(self, *args, **kwargs):
        return {}
