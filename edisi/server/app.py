"""
server/app.py

Server setup and routing is handled inside this file.
Implementation of routes should call methods from controller modules
"""

from flask import Flask, request

from edisi.controllers.registration import handle_register

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/register", methods=["POST"])
def register():
    handle_register(request)
