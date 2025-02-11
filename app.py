import os 
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import Flask, send_from_directory
from flask_mail import Mail, Message

load_dotenv()
app = Flask(__name__, static_folder="static", template_folder="templates")

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

# Route for another page
@app.route('/about')
def about():
    return render_template('generic.html')


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml', mimetype='application/xml')



@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    try:
        # Email to business
        msg_to_business = Message(
            subject=f"New message from {name}",
            sender=email,
            recipients=['mahletargaw1@gmail.com'],
            body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
        )
        mail.send(msg_to_business)

        # Confirmation email to customer
        msg_to_customer = Message(
            subject="Thank you for contacting us!",
            sender='mahletargaw1@gmail.com',
            recipients=[email],
            body=f"Hi {name},\n\nThank you for reaching out to us. We have received your message:\n\"{message}\"\n\nWe will get back to you shortly!\n\nBest regards,\nMaya Tech"
        )
        mail.send(msg_to_customer)

        # return jsonify({'message': 'Emails sent successfully!'})
        return redirect(url_for('index', success=True))
    except Exception as e:
        print(f"Error: {e}")
        # return jsonify({'error': 'Failed to send emails.'}), 500
        return redirect(url_for('index', success=True))

if __name__ == '__main__':
    app.run(debug=True)
