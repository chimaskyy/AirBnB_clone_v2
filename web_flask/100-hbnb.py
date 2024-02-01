#!/usr/bin/python3

""" Web app for hbnb content """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """
    Displays hbnb filters page
    """

    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places, users=users)


@app.teardown_appcontext
def tear_down(exception):
    """Cleans session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # places = storage.all(Place).values()

    # for place in places:
    #     print(place.name)
