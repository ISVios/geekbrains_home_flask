# from marshmallow_jsonapi import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field, field_for, fields

from blog.models.tag import TagModel


class TagSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TagModel
        include_fk = True


class TagWithoutIdSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TagModel
        include_fk = True
        dump_only = ("id",)
