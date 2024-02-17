#!/usr/bin/python3
""" this script start a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hbnb_c(text):
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def hbnb_py(text="is cool"):
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def hbnb_int(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def hbnb_int_render(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    # Start application
    app.run(host="0.0.0.0", port=5000, debug=True)
