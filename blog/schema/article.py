from datetime import datetime
from functools import partial

from marshmallow import INCLUDE, missing
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field, fields

from blog.models import ArticleModel
from blog.models.database import session
from blog.schema.author import AuthorSchema
from blog.schema.tag import TagSchema


class ArticleOutGetSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = session
        model = ArticleModel
        load_instance = True
        unknow = "INCLUDE"

    author = fields.Nested(
        AuthorSchema,
        missing=None,
        partial=True,
        default=None,
        server_default=None,
    )

    tags = fields.Nested(
        TagSchema(many=True), default=[], missing=[], server_default=[]
    )


class ArticleOutPostSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = session
        model = ArticleModel
        load_instance = True
        unknow = "INCLUDE"

    author = fields.Nested(
        AuthorSchema, missing=None, partial=True, default=None, server_default=None
    )

    title = auto_field(default="", missing="", server_default="", partial=True)
    body = auto_field(default="", missing="", server_default="", partial=True)

    tags = fields.Nested(
        TagSchema(many=True), default=[], missing=[], server_default=[]
    )

    dt_created = auto_field(
        allow_none=True,
        missing=datetime.now(),
        default=datetime.now(),
        server_default=datetime.now(),
        partial=True,
    )
    dt_updated = auto_field(
        allow_none=True,
        missing=datetime.now(),
        default=datetime.now(),
        server_default=datetime.now(),
        partial=True,
    )


class ArticleInPostSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = session
        model = ArticleModel
        load_instance = True
        unknow = "INCLUDE"

    author = fields.Nested(
        AuthorSchema,
        partial=True,
        required=True,
    )

    title = auto_field(required=True, partial=True)
    body = auto_field(required=True, partial=True)


class ArticleSchema(SQLAlchemyAutoSchema):
    class Meta:
        pass


class ArticleWithoutIdSchema(ArticleSchema):
    class Meta:
        sqla_session = session
        load_instance = True
        strict = True
        model = ArticleModel
        include_relationships = True
        # only_dump = ("dt_created",)
        exclude = ("id", "dt_created", "dt_updated")
        unknown = INCLUDE

    id = auto_field(
        partial=True, allow_none=True, missing=None, default=None, server_default=None
    )
    tags = fields.Nested(TagSchema(many=True), lazy="joined", missing=[])
    dt_created = auto_field(
        partial=True,
        missing=None,
    )
    dt_updated = auto_field(partial=True, missing=datetime.now())

    # author = fields.Nested(AuthorSchema, lazy="joined")
