from flask import Flask

app = Flask(__name__)

@app.route('/flask')

def my_fun():
    return 'Welcome to all of my dear friends...!!'

@app.route('/')

def my_fun_2():
    return 'Hello, welcome to flask framework...!!'

if __name__ == "__main__":
    app.run()