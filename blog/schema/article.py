from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields

from blog.models import ArticleModel
from blog.schema.author import AuthorSchema
from blog.schema.tag import TagSchema


class ArticleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ArticleModel

    tags = fields.Nested(TagSchema(many=True))

    author = fields.Nested(AuthorSchema)
