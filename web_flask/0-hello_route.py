#!/usr/bin/python3
"""
Script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
Use the option strict_slashes=False in your route definition
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Return Hello HBNB!
    """
    return "Hello HBNB!"


# app.run specified bc the code is ran using
# python3 -m web_flask.0-hello_route


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
