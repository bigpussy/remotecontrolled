from flask import Flask, request, render_template, redirect, url_for
from rgb import rgb
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route('/rgb.html', methods=['GET'])
def myrgb():
	if request.args['red']=='1':
		rgb(1,0,0)
	if request.args['red']=='0':
		rgb(0,0,0)
	return '1'

@app.route('/css/jquery.mobile-1.4.5.min.css')

def favicon():

	return redirect(url_for('css', filename='jquery.mobile-1.4.5.min.css'), code=301)

@app.route('/signin', methods=['POST'])
def signin():
	if request.form['username']=='admin' and request.form['password']=='password':
		rgb(1,1,1)
		return '<h3>Hello, admin!</h3>'
	return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
