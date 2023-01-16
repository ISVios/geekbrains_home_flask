import os
import logging

from flask import Flask, render_template
from werkzeug.exceptions import BadRequest

from flask_migrate import Migrate

from blog.security import flask_bcrypt
from blog.models import db, UserModel
from blog.views.user import users_app
from blog.views.article import article_app
from blog.views.auth import auth_app, login_manager

app: Flask = Flask(__name__)

# __Logger__
command_logger = logging.getLogger("command")
command_logger.setLevel("INFO")

# __CONFIG__
cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.config.{cfg_name}")

# __INIT__
flask_bcrypt.init_app(app)
db.init_app(app)
login_manager.init_app(app)

# __MIGRATE__
migrate = Migrate(app, db, compare_type=True)

# __CMD__


@app.cli.command("create-superuser")
def create_superuser():
    """
    create superuser root:toor
    password get from env ROOT_PASSWORD if env no found user 'toor'
    """
    from blog.models import UserModel

    root = UserModel(username="root", is_staff=True)
    root.password = os.environ.get("ROOT_PASSWORD") or "toor"

    db.session.add(root)
    db.session.commit()
    logging.info("create superuser: " + root)


# __BLUEPRINT__
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(article_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")


# __ROUTE__
@app.route("/")
def index():
    return render_template("index.html")
