from sqlalchemy import Column, Integer, String
from blog.models import db


class TagModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default="", server_default="")

    def __repr__(self) -> str:
        return f"<Tag #{self.id} {self.name}>"
