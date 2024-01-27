#!/usr/bin/python3
"""Starts a simple Flask web application"""
from flask import Flask, render_template
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
    return 'C ' + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def disp_python(text):
    """Displays dynamic content"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def disp_number(n):
    """Displays dynamic content"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def disp_numtemp(n):
    """Displays dynamic content"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
