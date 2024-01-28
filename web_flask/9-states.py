#!/usr/bin/python3
"""starts a Flask web application to dispaly a list of all states in storage"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def disp_states():
    """Route to display states list"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Route to display states by id"""
    state = storage.all(State).get('State.' + id)
    return render_template('state.html', state=state)


@app.teardown_appcontext
def teardownDB(exception):
    """Tears down the database and remove SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
