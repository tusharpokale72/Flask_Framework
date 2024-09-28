from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Your SMTP server
app.config['MAIL_PORT'] = 587  # For SSL
app.config['MAIL_USE_TLS'] = True  # Use TLS
app.config['MAIL_USERNAME'] = 'tusharpokale72@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'zftfqcgitultxwci'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = 'tusharpokale72@gmail.com'

mail = Mail(app)


@app.route('/send-email/')
def send_email():
    msg = Message("Hello from Flask",
                  recipients=["tusharpokale46@gmail.com"])  # List of recipients
    msg.body = "This is a test email sent from a Flask application."

    try:
        mail.send(msg)
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
