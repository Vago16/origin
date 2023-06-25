"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

DEF_IMG_URL = "https://img.icons8.com/?size=512&id=qeYxlZaoymoc&format=png"

class User (db.Model):
    """A Model for users of the blog"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable = False, default = DEF_IMG_URL)

    @property
    def full_name(self):
        """Returns the full name of user"""
        return f"{self.first_name} {self.last_name}"
    
    def connect_to_db(app):
        """Connects to Flask app"""
        db.app = app
        db.init_app(app)