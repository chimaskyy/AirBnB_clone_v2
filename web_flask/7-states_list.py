#!/usr/bin/python3
"""Importing Flask to run the web app
Routes for list of states. """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    """Remove the current SQLAlchemy Session
    after each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Render state_list html"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
