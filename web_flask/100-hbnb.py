#!/usr/bin/python3
"""
Script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes:
/hbnb_filters: display a HTML page like 6-index.html, which was done
during the project 0x01. AirBnB clone - Web static
Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css
and 8-places.css
from web_static/styles/ to the folder web_flask/static/styles
Copy files icon.png and logo.png from web_static/images/ to the
folder web_flask/static/images
Update .popover class in 6-filters.css to allow scrolling in the
popover and a max height of 300 pixels.
Use 6-index.html content as source code for the template 10-hbnb_filters.html
Replace the content of the H4 tag under each filter title
(H3 States and H3 Amenities) by &nbsp;
State, City and Amenity objects must be loaded from
DBStorage and sorted by name (A->Z)
"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """
    Remove current SQLAlchemy Session after each request
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def filters():
    """
    Display a HTML page like 8-index.html
    """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    sorted_states = sorted(states, key=lambda x: x.name)
    sorted_cities = sorted(cities, key=lambda x: x.name)
    sorted_amenities = sorted(amenities, key=lambda x: x.name)
    sorted_places = sorted(places, key=lambda x: x.name)

    return render_template('100-hbnb.html', states=sorted_states,
                           cities=sorted_cities, amenities=sorted_amenities,
                           places=sorted_places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
