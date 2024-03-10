from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/home')
def home():
    return "home"

@app.route('/admin')
def hello_admin():
    return "hello admin" 

@app.route('/guest/<name>')
def hello_guest(name):
    return "Welcome " + name

@app.route('/user/<username>')
def hello_username(username):
    if(username == "admin"):
        return redirect(url_for('hello_admin'))
    else:
        print(username)
        return redirect(url_for('hello_guest', name = username))
     
if __name__ == '__main__':
    app.run()
