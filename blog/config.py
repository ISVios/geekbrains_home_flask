import os
import logging

# __GLOBAL_Logger_Level__
# logging.basicConfig(level=logging.WARN)


class BaseConfig(object):
    Debug = False
    Testing = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevConfig(BaseConfig):
    Debug = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:////tmp/blog.db"
    )


class TestingConfig(BaseConfig):
    TESTING = True
