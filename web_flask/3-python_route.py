#!/usr/bin/python3
"""
This script creates a simple Flask web
application that responds with "Hello HBNB!" when accessed.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Route handler function for the root URL.

    Returns:
        str: A simple greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler function for the /hbnb URL.

    Returns:
        str: HBNB.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
@app.route('/c/', strict_slashes=False)
def c(text='is_cool'):
    """
    Route handler function for the /hbnb URL.

    Returns:
        str: c is cool or c <provided test>.
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text='is_cool'):
    """
    Route handler function for the /hbnb URL.

    Returns:
        str: Python is cool or Python <provided test>.
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
