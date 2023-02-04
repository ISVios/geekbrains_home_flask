from flask_apispec import MethodResource, doc, marshal_with, use_kwargs

from blog.models import ArticleModel
from blog.schema import ArticleSchema


@marshal_with(ArticleSchema(many=True))
@doc(tags=["Article"])
class ArticleList(MethodResource):
    def get(self):
        return ArticleModel.query.all()

    @use_kwargs(ArticleSchema)
    def put(self):
        return ArticleModel.query.all()


@doc(tags=["Article"])
class ArticleDetail(MethodResource):
    @use_kwargs(ArticleSchema)
    def get(self, id):
        return ArticleModel.query.filter(ArticleModel.id == id).one()

    @use_kwargs(ArticleSchema)
    def put(self, id):
        return {}
