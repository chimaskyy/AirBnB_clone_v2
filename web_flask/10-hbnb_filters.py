#!/usr/bin/python3
"""Importing Flask to run the web app
Routes for list of states. """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays HBnB filters HTML page."""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def tear_down(exception):
    """Remove the current SQLAlchemy Session
    after each request"""
    storage.close()




if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
