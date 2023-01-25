import logging
import os

from flask import Flask, render_template
from flask_migrate import Migrate
from werkzeug.exceptions import BadRequest

from blog.models import UserModel, db
from blog.security import flask_bcrypt
from blog.views.article import article_app
from blog.views.auth import auth_app, login_manager
from blog.views.author import author_app
from blog.views.user import users_app

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
    logging.info(f"create superuser: {root}")


@app.cli.command("create-tag")
def create_tag():
    """
    gen a common article tags
    """
    from blog.models import TagModel

    tag_list = [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
        "haskell",
        "rust",
        "vim",
        "neovim",
        "nim",
    ]
    for name in tag_list:
        tag = TagModel(name=name)
        db.session.add(tag)
    db.session.commit()
    logging.debug(f"{tag_list} created")


# __BLUEPRINT__
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(article_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(author_app, url_prefix="/authors")


# __ROUTE__
@app.route("/")
def index():
    return render_template("index.html")
