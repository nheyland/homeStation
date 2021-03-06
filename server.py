from smarthome import Plug
from ap import *
from flask import jsonify, Flask, request
from flask_cors import cross_origin
app = Flask(__name__)


@app.route("/america")
@cross_origin()
def america():
    metarmap().america()
    return "<p>success<P>"


@app.route("/metars")
@cross_origin()
def metar():
    metarmap().metars()
    return "<p>success<P>"


@app.route("/test")
@cross_origin()
def test():
    metarmap().test()
    return "<p>success<P>"


@app.route("/red")
@cross_origin()
def red():
    metarmap().red()
    return "<p>success<P>"


@app.route("/blue")
@cross_origin()
def blue():
    metarmap().blue()
    return "<p>success<P>"


@app.route("/green")
@cross_origin()
def green():
    metarmap().green()
    return "<p>success<P>"


@app.route("/off")
@cross_origin()
def off():
    metarmap().clear()
    return "<p>success<P>"


@app.route("/plug/printer")
@cross_origin()
def plugPrinter():
    Plug.toggle()
    return "<p>success<P>"


def run():
    app.run(host="0.0.0.0", port=3333)


run()
