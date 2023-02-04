import logging
from flask import Request, abort, session
from flask_login import current_user
from flask_restful import HTTPException


def need_authenticated(func):
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            abort(401)
        return func(*args, **kwargs)

    return wrapper


# Todo: find how get Meta withoy self or how make one class
# class AutoResourseMany(MethodResource):
#     def __init__(self, *args, **kwargs) -> None:
#         self.get.__apispec__["schemas"].append(self.Meta.schema)
#         # self.get.__apispec__["args"] = Annotation()
#         super().__init__(*args, **kwargs)
#
#     def get(self):
#         return {}
#
#     def post(self, **kwargs):
#         logging.critical(self.__dir__())
#         # logging.critical(self.get.__apispec__)
#
#
# def __getattribute__(self, __name: str):
#     if __name == "get":
#
#         @marshal_with(self.Meta.schema)
#         @need_authenticated
#         def _get():
#             return self.Meta.model.query.all()
#
#         return _get
#
#     elif __name == "post":
#
#         @marshal_with(self.Meta.schema)
#         @need_authenticated
#         def _post(**kwargs):
#             return self.Meta.model.query.all()
#
#         return _post
#
#     return super().__getattribute__(__name)
#
# @need_authenticated
# def __post(self, **kwargs):
#     enty = self.Meta.model(**kwargs)
#     db.session.add(enty)
#     db.session.commit()
#     return use_kwargs(self.Meta.schema), 201
#

# class AutoResourseOne(MethodResource):
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#
#     @need_authenticated
#     def get(self, id):
#         return self.Meta.model.query.all(), 200


def get_all(cls):
    """
    pattern get all elem of cls
    """
    return cls.query.all()


def get_by_id(cls, id):
    """
    pattern get elem by id of cls
    """
    enty = cls.query.filter(cls.id == id).one_or_none()
    if enty:
        return enty
    abort(404, description="no found.")


def post_method(cls, session, **kwargs):
    enty = cls(**kwargs)
    session.add(enty)
    session.commit()
    return enty, 201


def del_method(cls, session, id):
    enty = cls.query.filter(cls.id == id).one_or_none()
    if not enty:
        abort(404, description="no found.")
    session.delete(enty)
    session.commit()
    return {"message": "deleted."}, 201


def patch_method(cls, session, id, **kwargs):
    enty = cls.query.filter(cls.id == id).one_or_none()
    logging.critical(id)
    if not enty:
        abort(404, description="no found.")
    for key, value in kwargs.items():
        setattr(enty, key, value)
        session.add(enty)
        session.commit()
    return enty, 201
