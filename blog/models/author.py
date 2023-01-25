from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from blog.models import db


class AuthorModel(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_model.id"), nullable=False)

    user = relationship("UserModel", back_populates="author")
    article = relationship("ArticleModel", back_populates="author")

    def __repr__(self):
        return f"<author #{self.id} {self.user.username!r}>"
