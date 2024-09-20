from flask import Flask

app = Flask(__name__)

@app.route("/rout")

def my_fun():
    return "Hello welcome all, Ganpati Bappa Morya...!!"

if __name__ == "__main__":
    app.run()