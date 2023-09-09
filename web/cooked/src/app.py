from flask import Flask, Response, render_template, request, make_response
from base64 import b64encode, b64decode
import json
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    cookie = request.cookies.get('user')
    if cookie is None:
        resp = make_response(Response(open(__file__).read(), mimetype='text/plain'))
        resp.set_cookie('user', b64encode(bytes('{"username":"guest","uid":69}', 'utf-8')))
        return resp

    try:
        cookie = json.loads(b64decode(cookie).decode('utf-8'))
    except:
        resp = make_response(Response(open(__file__).read(), mimetype='text/plain'))
        resp.set_cookie('user', b64encode(bytes('{"username":"guest","uid":69}', 'utf-8')))
        return resp

    if cookie['username'] == 'admin' and cookie['uid'] == 0:
        return render_template('flag.html')

    resp = make_response(Response(open(__file__).read(), mimetype='text/plain'))
    resp.set_cookie('user', b64encode(bytes('{"username":"guest","uid":69}', 'utf-8')))
    return resp


app.run('0.0.0.0', os.environ['PORT'])
