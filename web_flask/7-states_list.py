#!/usr/bin/python3
""" Routes for list of states. """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Routes /states_list page."""
    from models import storage
    from models.state import State

    states = storage.all(State)
    states = dict(sorted(states.items(), key=lambda item: item[1]['name']))
    return render_template('7-states_list.html',
                           states=sorted(storage.all(State).values()))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
