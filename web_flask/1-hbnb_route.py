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
    Route handler function for the root URL.

    Returns:
        str: HBNB.
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
