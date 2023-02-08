# from marshmallow_jsonapi import Schema, fields
from blog.models.database import session
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field, field_for, fields

from blog.models.tag import TagModel


class TagSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = session
        model = TagModel
        load_instance = True
        strict = True
        session = session


class TagWithoutIdSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = session
        model = TagModel
        load_instance = True
        strict = True
        dump_only = ("id",)
