#!/usr/bin/python3
"""
This script creates a simple Flask web
application that responds with "Hello HBNB!" when accessed.
"""

from flask import Flask
from flask import render_template

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
    Route handler function for the /c/.

    Returns:
        str: c is cool or c <provided test>.
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text='is_cool'):
    """
    Route handler function for the /pyton/.

    Returns:
        str: Python is cool or Python <provided test>.
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route handler function for the /number/n

    Returns:
        str: <n> is a number or 404.
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer
    showing if number is odd or even
    """
    if isinstance(n, int):
        return render_template(
            '6-number_odd_or_even.html',
            n=n, parity='even' if n % 2 == 0 else 'odd'
        )
    else:
        return 'Not an integer', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
