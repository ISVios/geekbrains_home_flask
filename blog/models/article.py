from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, Text, func
from sqlalchemy.orm import relationship

from blog.models import db
from blog.models.article_tag import article_tag_table


class ArticleModel(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author_model.id"))
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship("AuthorModel", back_populates="article")
    tags = relationship(
        "TagModel", secondary=article_tag_table, back_populates="articles"
    )

    def __str__(self) -> str:
        return str(self.title)
