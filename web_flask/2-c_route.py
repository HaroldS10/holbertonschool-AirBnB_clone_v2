#!/usr/bin/python3


"""
The module creates a script that starts a Flask web application
"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
# We use route() decorator to tell Flask which URL should trigger our function
def first_route():
    return'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def define_route():
    return'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def print_text(text):
    return f'C {escape(text)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
