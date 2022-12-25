from flask import Flask, render_template
from werkzeug.exceptions import BadRequest


from blog.models import db
from blog.views.user import users_app
from blog.views.article import article_app

app: Flask = Flask(__name__)


# __CONFIG__

# __DB__
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# __BLUEPRINT__
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(article_app, url_prefix="/articles")


# __ROUTE__
@app.route("/")
def index():
    return render_template("index.html")
