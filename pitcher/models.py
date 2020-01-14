from datetime import datetime
from pitcher import db, login_manager

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    img_file = db.Column(db.String(20), default="default.jpg")
    password = db.Column(db.String(60),  nullable=False)
    posts = db.relationship("Pitch", backref="author", lazy=True)

    def __repl__(self):
        return f"User({self.username}, {self.email}, {self.img_file})"

class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


    def __repl__(self):
        return f"Pitch({self.title}, {self.date_posted}, {self.img_file})"
