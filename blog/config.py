import os
import logging

# __GLOBAL_Logger_Level__
logging.basicConfig(level=os.environ.get("LOGGER_LEVEL", None))


class BaseConfig(object):
    Debug = False
    Testing = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    WTF_CSRF_ENABLED = True


class DevConfig(BaseConfig):
    Debug = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:////tmp/blog.db"
    )


class TestingConfig(BaseConfig):
    TESTING = True
