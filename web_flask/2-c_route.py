#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Display a web aplication."""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Display a web aplication."""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """Display a web aplication."""
    ret = "C {}".format(text)
    return ret.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
