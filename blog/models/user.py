from sqlalchemy import Column, Integer, String, Boolean
from blog.models import db


class UserModel(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)


def __repr__(self):
    return f"<User #{self.id} {self.username!r}>"
