# from marshmallow_jsonapi import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from blog.models.tag import TagModel


class TagSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TagModel
