#!/usr/bin/python3
""" Routes for list of states. """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
states = storage.all(State)


@app.route('/states_list', strict_slashes=False)
def states_list(states):
    """ Routes /states_list page."""

    return render_template('7-states_list.html',
                           states=sorted(storage.all(State).values()))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
