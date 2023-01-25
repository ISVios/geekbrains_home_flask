from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from blog.models import db
from blog.models.article_tag import article_tag_table


class TagModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default="", server_default="")

    articles = relationship(
        "ArticleModel", secondary=article_tag_table, back_populates="tags"
    )

    def __repr__(self) -> str:
        return f"<Tag #{self.id} {self.name}>"
