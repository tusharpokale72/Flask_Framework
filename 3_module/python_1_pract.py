from flask import Flask,render_template

app = Flask(__name__)

@app.route('/cars')

def result():
    my_cars = {"Tata":85000,'Scorpio':56000,'mercediz':86000,'Hyundai':75000,'Thar':65000}
    return render_template("home_1.html",result = my_cars)


if __name__ == "__main__":
    app.run()