from marshmallow_jsonapi import Schema, fields
from flask_apispec import marshal_with, use_kwargs

from blog.models.tag import TagModel


class TagSchema(Schema):
    class Meta:
        type_ = "tag"
        fields = ("id", "name")

    id = fields.Integer(as_string=True)
    name = fields.String(allow_none=False, required=True)
