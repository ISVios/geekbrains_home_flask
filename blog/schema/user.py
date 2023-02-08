from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from blog.models.user import UserModel


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        exclude = ("_password",)


class UserWithoutIdSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        exclude = ("_password",)
        dump_only = ("id",)

    is_staff = fields.Boolean(load_default=False)

    username = auto_field(required=False)

    # ToDo: find how hide fields, or set empty value
    # Try^: "partial" param
    # new_password = fields.String(required=False, load_default="", allow_none=True)
    # new_password_dup = fields.String(required=False, load_default="", allow_none=True)
