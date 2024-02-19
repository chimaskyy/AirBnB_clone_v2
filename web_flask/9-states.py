#!/usr/bin/python3
"""Importing Flask to run the web app
Routes for list of states. """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    """Remove the current SQLAlchemy Session
    after each request"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Render state_list html"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states, mode='allState')


@app.route("/states/<id>", strict_slashes=False)
def state_with_id(id):
    """Render state_list html if state
    is found with id passed"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state, mode='id')
    return render_template("9-states.html", state=state, mode='none')


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
