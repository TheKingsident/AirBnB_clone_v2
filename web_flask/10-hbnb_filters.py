#!/usr/bin/python3
"""starts a Flask web application to dispaly a list of all states in storage"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def disp_states():
    """Route to display states list"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardownDB(exception):
    """Tears down the database and remove SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
