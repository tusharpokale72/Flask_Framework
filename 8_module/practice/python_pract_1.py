from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

app.route('/')
def home():
    return render_template('index.html')

app.route('/enternew')
def newrec():
    return render_template('student.html')

app.route('/addrec',methods=['GET','POST'])
def addrec():
    global msg
    if request.method=='POST':

