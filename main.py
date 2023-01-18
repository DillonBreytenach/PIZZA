import flask
from flask import Flask
import os
import sys
from flask import render_template

app = Flask(__name__)


@app.route('/') #, method=["GET","POST"])
def main():
    print("HELLO")
    return "HELLO"


@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('index.html')


if __name__=="__main__":
    #app.config['SERVER_NAME'] = 'bossref.com:5000'
    app.run(host='0.0.0.0', port=81)