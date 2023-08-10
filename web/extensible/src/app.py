from flask import Flask, request, redirect, url_for, render_template, make_response
from hashlib import md5
from lxml import etree
import secrets
import sqlite3
import os


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('dashboard'), 301)


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/api/register', methods=['POST'])
def register_api():
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    if request.cookies.get('session') is not None:
        check_cookie = "SELECT username FROM users WHERE session=?"

        if cur.execute(check_cookie, (request.cookies.get('session'),)).fetchone() is not None:
            con.commit()
            con.close()
            return 'Already logged in:<a href="/dashboard">Dashboard</a>'

    xml = request.get_data()
    parser = etree.XMLParser(no_network=False)
    try:
        doc = etree.fromstring(xml, parser) 
        check_exists = "SELECT username FROM users WHERE username=?"

        if cur.execute(check_exists, (doc.find('username').text,)).fetchone() is not None:
            con.commit()
            con.close()
            return 'Username already exists'

        register_user = "INSERT INTO users (username, password) VALUES (?, ?)"
        cur.execute(register_user, (doc.find('username').text, md5(bytes(doc.find('password').text, 'utf-8')).hexdigest(),))
    except Exception:
        con.commit()
        con.close()
        return 'An error has occurred'

    con.commit()
    con.close()
    return 'User successfully registered'


@app.route('/api/login', methods=['POST'])
def login_api():
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    if request.cookies.get('session') is not None:
        check_cookie = "SELECT username FROM users WHERE session=?"

        if cur.execute(check_cookie, (request.cookies.get('session'),)).fetchone() is not None:
            con.commit()
            con.close()
            return 'Already logged in:<a href="/dashboard">Dashboard</a>'

    xml = request.get_data()
    parser = etree.XMLParser(no_network=False)
    try:
        doc = etree.fromstring(xml, parser)
        check_auth = "SELECT username FROM users WHERE username=? AND password=?"

        if cur.execute(check_auth, (doc.find('username').text, md5(bytes(doc.find('password').text, 'utf-8')).hexdigest(),)).fetchone() is None:
            con.commit()
            con.close()
            return 'Incorrect username or password'
        session = secrets.token_hex(16)
        add_cookie = "UPDATE users SET session=? WHERE username=?"
        cur.execute(add_cookie, (session, doc.find('username').text,))
    except Exception:
        con.commit()
        con.close()
        return 'An error has occurred'

    r = make_response('Successfully logged in:<a href="/dashboard">Dashboard</a>')
    r.set_cookie('session', session, path='/')

    con.commit()
    con.close()

    return r


@app.route('/dashboard', methods=['GET'])
def dashboard():
    if request.cookies.get('session') is None:
        return redirect(url_for('login'))

    con = sqlite3.connect('users.db')
    cur = con.cursor()
    username = cur.execute('SELECT username FROM users WHERE session=?', (request.cookies.get('session'),)).fetchone()
    con.close()

    if username is not None:
        return render_template('home.html', name=username[0])

    return redirect(url_for('login'))


app.run('0.0.0.0', os.environ['PORT'])
