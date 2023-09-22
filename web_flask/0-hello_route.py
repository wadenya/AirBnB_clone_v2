#!/usr/bin/python3
"""Start Flsak web application.
"""

from flask import Flask

myapp = Flask(__name__)

#define route for root url
@myapp.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

if __name__ == "__main__":
	#listen on all available network interface 0.0.0.0 and port 5000
	myapp.run(host='0.0.0.0', port=5000)
