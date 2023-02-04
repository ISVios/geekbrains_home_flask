from flask_apispec import MethodResource, doc, marshal_with, use_kwargs

from blog.models import ArticleModel
from blog.models.database import session
from blog.schema import ArticleSchema
from blog.schema.article import ArticleWithoutIdSchema
from blog.api.database import get_all, get_by_id, patch_method, need_authenticated


@doc(tags=["Article"])
class ArticleList(MethodResource):
    @marshal_with(ArticleSchema(many=True))
    @need_authenticated
    def get(self):
        return get_all(ArticleModel)


@doc(tags=["Article"])
class ArticleDetail(MethodResource):
    @use_kwargs(ArticleSchema)
    @need_authenticated
    def post(self):
        return ArticleModel.query.all()

    @marshal_with(ArticleSchema)
    @need_authenticated
    def get(self, id):
        return get_by_id(ArticleModel, id)

    @use_kwargs(ArticleWithoutIdSchema)
    @marshal_with(ArticleSchema)
    @need_authenticated
    def patch(self, id, kwargs):
        # ToDo think or ask whitch fields neeed
        return patch_method(ArticleModel, session, id, **kwargs)
