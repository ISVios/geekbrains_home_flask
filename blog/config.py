import os
import logging

from flask_apispec.extension import APISpec, MarshmallowPlugin

# __GLOBAL_Logger_Level__
logging.basicConfig(level=os.environ.get("LOGGER_LEVEL", None))


class BaseConfig(object):
    Debug = False
    Testing = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    WTF_CSRF_ENABLED = True
    APP_API_VERSION = "v1"
    OPENAPI_URL_PREFIX = "/api/swagger"
    OPENAPI_SWAGGER_UI_VERSION = "2.0.0"
    APISPEC_SPEC = APISpec(
        "blog.app",
        APP_API_VERSION,
        OPENAPI_SWAGGER_UI_VERSION,
        [MarshmallowPlugin()],
    )
    APISPEC_SWAGGER_URL = None  # "/api/"
    APISPEC_SWAGGER_UI_URL = None  # OPENAPI_URL_PREFIX


class DevConfig(BaseConfig):
    Debug = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:////tmp/blog.db"
    )


class TestingConfig(BaseConfig):
    TESTING = True
