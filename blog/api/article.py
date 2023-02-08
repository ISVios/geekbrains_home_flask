from datetime import datetime
from logging import critical

from flask import abort
from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from flask_login import current_user
from flask_sqlalchemy.model import Model
from flask_wtf.csrf import logging
from marshmallow import INCLUDE
from sqlalchemy import inspect

from blog.api.database import (
    del_method,
    get_all,
    get_by_id,
    need_authenticated,
    patch_method,
)
from blog.models import ArticleModel
from blog.models.database import session
from blog.models.tag import TagModel
from blog.models.user import UserModel
from blog.schema import ArticleSchema, author
from blog.schema.article import (
    ArticleInPostSchema,
    ArticleOutGetSchema,
    ArticleOutPostSchema,
    ArticleWithoutIdSchema,
)
from blog.schema.tag import TagSchema


@doc(tags=["Article"])
class ArticleFunc(MethodResource):
    def get(self):
        return {"count": ArticleModel.query.count()}


@doc(tags=["Article"])
class ArticleList(MethodResource):
    @marshal_with(ArticleOutGetSchema(many=True))
    @need_authenticated()
    def get(self):
        return get_all(ArticleModel)

    @marshal_with(ArticleOutPostSchema(many=True))
    @use_kwargs(ArticleInPostSchema(many=True))
    @need_authenticated()
    def post(self, *objs, **kwargs):
        for obj in objs:
            session.add(obj)
        session.commit()
        return ArticleModel.query.all()


@doc(tags=["Article"])
class ArticleDetail(MethodResource):
    @marshal_with(ArticleSchema)
    @need_authenticated()
    def get(self, id):
        return get_by_id(ArticleModel, id)

    @marshal_with(ArticleSchema)
    @use_kwargs(ArticleWithoutIdSchema)
    @need_authenticated()
    def patch(self, *obj, **kwargs):
        # ToDo think or ask whitch fields neeed
        # test who make this article
        article = ArticleModel.query.get(kwargs["id"])
        if article:
            # if you root ok else test you make this article.
            if not current_user.is_staff:
                # get author->user from article
                same_user = article.author.user == current_user
                if not same_user:
                    abort(401, description="You can't change this article.")
        else:
            abort(404)

        obj = obj[0]

        # patch Article
        # restory TagModel

        # ToDo: think : logic if not found tags (**ignore** | create)
        tags_names_ = [tag.name for tag in obj.tags]

        obj.tags = TagModel.query.filter(TagModel.name.in_(tags_names_)).all()
        if len(tags_names_) != len(obj.tags):
            logging.warning(
                f"Can`t add some tags{tags_names_}|{obj.tags} to {article} "
            )

        article.update(obj)
        session.commit()
        return article

    @need_authenticated()
    def delete(self, id):
        return del_method(ArticleModel, session, id)
