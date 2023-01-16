from sqlalchemy import Column, Integer, LargeBinary, String, Boolean
from blog.models import db
from flask_login import UserMixin

import flask_bcrypt


class UserModel(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), nullable=False, default="", server_default="")
    _password = Column(LargeBinary, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = flask_bcrypt.generate_password_hash(val)

    def password_vildate(self, password):
        return flask_bcrypt.check_password_hash(self._password, password)

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
