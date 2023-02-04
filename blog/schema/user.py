from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from blog.models.user import UserModel


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        exclude = ("_password",)
