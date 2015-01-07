from flask import Flask, request, render_template
from rgb import rgb
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route('/rgb.html', methods=['GET'])
def rgb():
	#print request.form['red']
	return '''<form action="/signin" method="post">
	              <p><input name="username"></p>
		                    <p><input name="password" type="password"></p>
				                  <p><button type="submit">Sign In</button></p>
						                </form>'''

@app.route('/signin', methods=['POST'])
def signin():
	if request.form['username']=='admin' and request.form['password']=='password':
		rgb(1,1,1)
		return '<h3>Hello, admin!</h3>'
	return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
