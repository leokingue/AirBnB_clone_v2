#!/usr/bin/python3
from flask import Flask
"""
Write a script that starts a Flask web application:
"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello_1():
    """Display 'Hello HBNB' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_2():
    """Display 'HBNB' """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
