#!/usr/bin/python3
"""
Script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text
/python/<text>: display “Python ”, followed by the value of text
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
"""


from flask import Flask, abort, render_template


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


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """
    Display “n is a number” only if n is an integer
    """
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """
    Display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    """
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        abort(404)


# app.run specified bc the code is ran using
# python3 -m web_flask.0-hello_route


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
