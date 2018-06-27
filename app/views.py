# cong:utf-8

from flask import jsonify
from flask import render_template
import json
from flask import Flask, make_response, redirect, abort

from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=['GET', ])
def hello():
    return jsonify(msg="hello world!")


@app.route('/json')
def do_json():
    hello = {"name":"stranger", "say":"hello"}
    return json.dumps(hello)


@app.route('/status_500')
def status_500():
    return "hello",500


@app.route('/set_header')
def set_header():
    resp = make_response('<h1>This document has a modified header!</h1>')
    resp.headers['X-Something'] = 'A value'
    resp.headers['Server'] = 'My special http server'
    return resp


@app.route('/set_cookie')
def set_cookie():
    resp = make_response('<h1>This document carries a cookie!</h1>')
    resp.set_cookie('username', 'evancss')
    return resp


@app.route('/redir')
def redir():
    return redirect('http://www.baidu.com')


@app.route('/user/<id>')
def get_user(id):
    if int(id)>10:
        abort(404)
    return '<h1>Hello, %s</h1>' % id