from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound


users_app = Blueprint("users_app", __name__)
USER = {
    1: "User1",
    2: "User2",
    3: "User3",
    4: "User4",
    5: "User5",
}


@users_app.route("/", endpoint="list")
def users_list():
    return render_template("user/list.html", users=USER)


@users_app.route("/<int:user_index>/", endpoint="detail")
def user_detail(user_index: int):
    try:
        user_name = USER[user_index]
    except KeyError:
        raise NotFound(f"User #{user_index} no found.")
    return render_template(
        "user/detail.html", user_index=user_index, user_name=user_name
    )
