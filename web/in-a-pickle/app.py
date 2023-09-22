import pickle
import base64
from flask import Flask, Response, render_template, request, make_response
import os
from base64 import b64encode, b64decode
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    resp = make_response(Response(open(__file__).read(), mimetype='text/plain'))
    return resp

@app.route("/vuln", methods=["POST"])
def vuln():
    data = base64.urlsafe_b64decode(request.form['pickled'])
    deserialized = pickle.loads(data)
    return 0

app.run('0.0.0.0',os.environ['PORT'])
