#!/usr/bin/python3
"""
Script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes:
/states: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in
DBStorage sorted by name (A->Z)
LI tag: description of one State: <state.id>: <B><state.name></B>
/states/<id>: display a HTML page: (inside the tag BODY)
If a State object is found with this id:
H1 tag: “State: ”
H3 tag: “Cities:”
UL tag: with the list of City objects linked to the State sorted by name (A->Z)
LI tag: description of one City: <city.id>: <B><city.name></B>
Otherwise:
H1 tag: “Not found!”
You must use the option strict_slashes=False in your route definition
"""


from models import storage
from models.state import State
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
    sorted_states = sorted(states, key=lambda x: x.name)
    print(sorted_states)
    return render_template('9-states.html', states=sorted_states, flag=True)


@app.route("/states/<id>", strict_slashes=False)
def states(id):
    """
    Display a HTML page with list of all state obj in dbstorage
    sorted by name
    """
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state, flag=False)
    else:
        return render_template('9-states.html', state=None, flag=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
