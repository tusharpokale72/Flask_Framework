from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def student_info():
    return render_template('student_1.html')

@app.route('/result',methods=['POST','GET'])
def my_result():
    if request.method=='POST':
        my_result = request.form
        return render_template('result.html',result=my_result)

if __name__=="__main__":
    app.run()