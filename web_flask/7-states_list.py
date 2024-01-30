#!/usr/bin/python3
""" Routes for list of states. """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Routes /states_list page."""

    states = storage.all(State)
    return render_template('7-states_list.html',
                           states=states.values())


@app.teardown_appcontext
def tear_down(exception):
    """ Cleans up session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
