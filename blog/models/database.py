from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()

session = db.session

__all__ = ["db", "session"]
