#!/usr/bin/python3
"""
Script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage
sorted by name (A->Z)
LI tag: description of one State: <state.id>: <B><state.name></B>
"""


from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """
    Remove current SQLAlchemy Session after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Display a HTML page with list of all state obj in dbstorage
    sorted by name
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
