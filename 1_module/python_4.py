from flask import Flask

app = Flask(__name__)

@app.route("/")

def my_fun():
    return "Enter your Name: "

@app.route('/<name>')

def hello_name(name):
    return 'My Name is %s, Welcome to data science batch 2024'% name

if __name__ == "__main__":
    app.run()
