from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'please enter your name in tool bar: '

@app.route('/hello/<name>')
def hello_Name(name):
    return 'Hello %s, Welcome to the Data Science Class...!!' % name


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5050,debug=True)