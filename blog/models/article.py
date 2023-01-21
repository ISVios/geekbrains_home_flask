from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from blog.models import db


class ArticleModel(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author_model.id"))

    author = relationship("AuthorModel", back_populates="articles")
