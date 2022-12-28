from sqlalchemy import Column, Integer, String, Boolean
from blog.models import db
from flask_login import UserMixin


class UserModel(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), nullable=False, default="", server_default="")
    is_staff = Column(Boolean, nullable=False, default=False)


def __repr__(self):
    return f"<User #{self.id} {self.username!r}>"
