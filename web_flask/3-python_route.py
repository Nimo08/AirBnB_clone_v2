#!/usr/bin/python3
"""
Script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text
/python/<text>: display “Python ”, followed by the value of the
text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
variable (replace underscore _ symbols with a space )
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


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Return HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    Display “C ” followed by the value of the text variable
    """
    if "_" in text:
        text_var = text.replace("_", " ")
    else:
        text_var = text
    return "C %s" % text_var


# use 2 app.routes bc of default text
@app.route("/python", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """
    Display “Python ”, followed by the value of the text variable
    """
    if "_" in text:
        text_var = text.replace("_", " ")
    else:
        text_var = text
    return f"Python {text_var}"

# app.run specified bc the code is ran using
# python3 -m web_flask.0-hello_route


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
