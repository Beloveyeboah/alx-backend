#!/usr/bin/env python3

"""
First you will setup a basic Flask app in 0-app.py
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """Route for the index page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
