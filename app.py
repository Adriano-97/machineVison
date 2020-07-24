from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

# Var declarations
ENV = ''

# Select Enviroment
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:adry@localhost/feedback'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ojqwvevbrqphtg:cd5b1d7cfd77e2a61bc3b975a3a15b894ddd90b176b00a503273b347b6741d04@ec2-34-193-42-173.compute-1.amazonaws.com:5432/d4bha82e2pd9kl'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Data Models
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(200))
    reason = db.Column(db.String(200))
    rating = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, user, reason, rating, comments):
        self.comments = comments
        self.user = user
        self.rating = rating
        self.reason = reason

# Defining Routes
@app.route('/')
def index():
        return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        reason = request.form['reason']
        rating = request.form['rating']
        comments = request.form['comments']
        # Validating input
        if user == '' or reason == '':

            return render_template('index.html', message='Please enter required fields')
        data = Feedback(user, reason, rating, comments)
        db.session.add(data)
        db.session.commit()
        send_mail(user, reason, rating, comments)
        # After Feedback is provided move to success page
        return render_template('success.html')

if __name__ == '__main__':
        
        app.run()
