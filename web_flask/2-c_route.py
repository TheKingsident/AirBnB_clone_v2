#!/usr/bin/python3
"""Starts a simple Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Displays content"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def disp_hbnb():
    """Displays content"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def disp_text(text):
    """Displays dynamic content"""
    return 'C '+ text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
