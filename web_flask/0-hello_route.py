#!/usr/bin/python3

"""
The module creates a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False) # We use the route() decorator to tell Flask which URL should trigger our function.
def hello_world():
    return ("Hello HBNB!")

if __name__ = '__main__':
    app.run(host= '0.0.0.0', port= 5000)