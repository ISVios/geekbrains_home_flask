from sqlalchemy import Table, Column, Integer, ForeignKey

from blog.models import db

article_tag_table = Table(
    "article_tag_table",
    db.metadata,
    Column("article_id", Integer, ForeignKey("article_model.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tag_model.id"), nullable=False),
)
