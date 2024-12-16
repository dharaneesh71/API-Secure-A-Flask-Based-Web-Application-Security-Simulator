from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bleach

app = Flask(__name__)

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_security.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize the rate limiter with in-memory storage
limiter = Limiter(
    key_func=get_remote_address
)
limiter.init_app(app)

# User table model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Log table to track attack attempts
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attack_type = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

# Function to log attacks in the database
def log_attack(attack_type):
    log = Log(attack_type=attack_type)
    db.session.add(log)
    db.session.commit()

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# SQL Injection simulation
@app.route('/vulnerable_sql', methods=['POST'])
def vulnerable_sql():
    username = request.form['username']
    password = request.form['password']

    # Simulate SQL Injection
    if username == "' OR '1'='1":
        log_attack("SQL Injection Attempt")
        return jsonify({"message": "SQL Injection detected!"}), 400
    elif username == "admin" and password == "password":
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Login failed!"}), 401

# XSS simulation
@app.route('/vulnerable_xss', methods=['POST'])
def vulnerable_xss():
    comment = request.form['comment']

    # Clean input to prevent XSS
    clean_comment = bleach.clean(comment)
    log_attack("XSS Attempt")
    return jsonify({"message": "Comment received!", "comment": clean_comment})

# Rate-limited DoS prevention
@app.route('/rate_limited_api', methods=['GET'])
@limiter.limit("5 per minute")
def rate_limited_api():
    return jsonify({"message": "This is a rate-limited API."})

# Route to view attack logs
@app.route('/logs', methods=['GET'])
def view_logs():
    logs = Log.query.all()
    return render_template('logs.html', logs=logs)

# Route to clear attack logs
@app.route('/clear_logs', methods=['POST'])
def clear_logs():
    db.session.query(Log).delete()  # Delete all logs from the database
    db.session.commit()  # Commit the changes to the database
    return redirect(url_for('view_logs'))  # Redirect back to the logs page

# Run the app
if __name__ == '__main__':
    with app.app_context():  # Set up application context
        db.create_all()  # Create database tables
    app.run(debug=True)
