from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, field_for, fields
from blog.models import AuthorModel
from blog.schema import UserSchema


class AuthorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AuthorModel

    user = fields.Nested(UserSchema)
