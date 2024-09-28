from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail = Mail(app)

# Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Use 587 for TLS
app.config['MAIL_USERNAME'] = os.environ.get('tusharpokale72@gmail.com')  # Set in your environment
app.config['MAIL_PASSWORD'] = os.environ.get('Tushar@0309')  # Set in your environment
app.config['MAIL_USE_TLS'] = True  # Use TLS
app.config['MAIL_USE_SSL'] = False  # Do not use SSL

@app.route('/')
def index():
    try:
        msg = Message("Hello", sender=app.config['MAIL_USERNAME'], recipients=['tusharpokale72@gmail.com'])
        msg.body = 'Hello Flask Message sent from Flask-Mail'
        mail.send(msg)
        return 'Email sent successfully!'
    except Exception as e:
        return f'Failed to send email: {str(e)}'

if __name__ == "__main__":
    app.run(debug=True)

