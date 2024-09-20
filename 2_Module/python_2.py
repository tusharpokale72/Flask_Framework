from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Admin and Guest Login Screen...!!'

@app.route('/admin')
def hello_admin():
    return "Hello Admin, Welcome to the Flask Framework..!!"

@app.route('/guest')
def hello_guest():
    return "Hello %s, Welcome to the Flask Framework..!!"


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    elif name == 'guest' :
        return redirect(url_for('hello_guest'))
    else:
        return 'hello frnds'

if __name__=="__main__":
    app.run(debug=True)