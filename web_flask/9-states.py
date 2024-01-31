#!/usr/bin/python3
"""
Web App that extracts data from FileStorage or DBstorage and routes
them to URL.
"""

from flask import Flask, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Routes page for list of states"""

    states = storage.all(State)

    if id and ('State.' + id) in states.keys():
        id = 'State.' + id
        return render_template('9-states.html', states=states, id=id)
    elif id and ('State.' + id) not in states.keys():
        return "<H1>Not Found</H1>"
    return render_template('9-states.html', states=states.values())


@app.teardown_appcontext
def tear_down(exception):
    """Cleans up session after each request"""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
