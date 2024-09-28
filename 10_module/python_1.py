from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'tusharpokale72@gmail.com'
app.config['MAIL_PASSWORD'] = 'zftfqcgitultxwci'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    msg = Message("Hello welcome", sender='tusharpokale72@gmail.com', recipients=['tusharpokale46@gmail.com'])
    msg.body = 'Hello Flask Message sent from Flask-Mail_2'
    mail.send(msg)
    return 'sent mail successfully'


if __name__=="__main__":
    app.run()

