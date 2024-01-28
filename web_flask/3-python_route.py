#!/usr/bin/python3
"""
flask app Routes /c/
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ routes the root of the URL """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ routes /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ routes /c/<text> where text is any string """

    if text:
        text = text.replace('_', ' ')
        return "C {}".format(text)
    return "C"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ routes /python/<text> """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
