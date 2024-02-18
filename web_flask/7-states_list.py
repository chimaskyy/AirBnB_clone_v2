#!/usr/bin/python3


from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
storage.close()

@app.route("/states_list", strict_slashes=False)
def states():
    return render_template("7-states_list.html")

