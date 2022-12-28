import os

from flask import Flask, render_template
from werkzeug.exceptions import BadRequest

from flask_migrate import Migrate

from blog.models import db, UserModel
from blog.views.user import users_app
from blog.views.article import article_app
from blog.views.auth import auth_app, login_manager

app: Flask = Flask(__name__)

# __CONFIG__
# app.config["SECRET_KEY"] = "^8wg6yjji4@2ur^41jq6g9hw%4q(77&jgc#zmzlh%v_959lf6)"
cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.config.{cfg_name}")

# __DB__
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# __INIT__
db.init_app(app)
login_manager.init_app(app)

# __MIGRATE__
migrate = Migrate(app, db)

# __CMD__
@app.cli.command("init-db")
def init_db():
    """Init empty db"""
    db.create_all()
    print("init db. Done.")


@app.cli.command("full-db")
def full_db():
    """
    Crete 3 users ->
    user1
    user2
    root (superuser)
    """
    root = UserModel(username="root", is_staff=True)
    user1 = UserModel(username="user1")
    user2 = UserModel(username="user2")

    db.session.add(root)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("Created ->\nuser1\t\nuser2\t\nroot\t(superuse)")


# __BLUEPRINT__
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(article_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")


# __ROUTE__
@app.route("/")
def index():
    return render_template("index.html")
