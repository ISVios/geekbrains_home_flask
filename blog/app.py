from flask import Flask, request
from werkzeug.exceptions import BadRequest

app: Flask = Flask(__name__)


@app.route("/")
def index():
    return "Hello world", 200


@app.route("/power")
def power():
    x = request.args.get("x", "")
    y = request.args.get("y", "")

    if not (x.isdigit() and y.isdigit()):
        app.logger.info(f"in '/power' x or y no digit. x={x} y={y}")
        return BadRequest("No found x or y param")

    x = int(x)
    y = int(y)
    result = x**y
    app.logger.info(f"open '/power' {x} ^ {y} = {result}")
    return str(result)


@app.errorhandler(ZeroDivisionError)
def handle_zero_div_error(error):
    app.logger.error(error)
    return "<h1>Please don't forget close darkhole by youself</h1>", 400


@app.route("/inf")
def inf():
    return str(1 / 0)
