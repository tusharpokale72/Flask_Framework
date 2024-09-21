from flask import  Flask

app = Flask(__name__)

@app.route('/posting/<post>')
def index(post):
    return "My post is %s" %post

@app.route('/rev/<float:number>')
def add(number):
    return "Addition of First Number %f " %number

if __name__=="__main__":
    app.run()