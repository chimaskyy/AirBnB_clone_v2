#!/usr/bin/python3
"""
flask app Routes /, /c/, python, /n
"""

from flask import Flask, abort, render_template

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


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """ routes /number/<n>"""
    if type(eval(n)) == int:
        return "{} is a number".format(n)
    abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """ routes /number/<n>"""
    try:
        if type(eval(n)) == int:
            return render_template('5-number.html', number=n)
        else:
            abort(404)
    except NameError as e:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
