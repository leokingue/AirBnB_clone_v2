#!/usr/bin/python3
from flask import Flask, escape, render_template
"""
Write a script that starts a Flask web application:
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_1():
    """ Display 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_2():
    """Display 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """Display "C" followed by the value"""
    str_1 = ('_', ' ')
    if text.find(str_1[0]) != -1:
        new_str = text.replace(str_1[0], str_1[1])
        return 'C {}'.format(new_str)
    else:
        return 'C {}'.format(escape(text))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    """display "python", followed by the value of the
    variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """Display a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """ display a HTML page only if n is an integer """
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
