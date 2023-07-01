"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy

DEF_IMG_URL = "https://img.icons8.com/?size=512&id=qeYxlZaoymoc&format=png"

class User (db.Model):
    """A Model for users of the blog"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable = False, default = DEF_IMG_URL)

    posts = db.relationship("Post", backref = "user", cascade = "all, delete-orphan")

    @property
    def full_name(self):
        """Returns the full name of user"""
        return f"{self.first_name} {self.last_name}"
    

class Post (db.Model):
    """A model for blog posts"""
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    
    user = db.relationship('User')

    @property
    def friendly_date(self):
        """Show a friendly-looking version of the date as a string, like “May 1, 2015, 10:30 AM”"""
        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")
    
class Tag(db.Model):
    """A tagging feature that can be added to posts"""
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Integer, nullable = False, unique = True)

    posts = db.relationshio('Post', secondary = "post_tags", backref= "tags")

class PostTag(db.Model):
     """Model that joins together a Post and Tag"""
     __tablename__ = "post_tags"

     post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key = True)
     tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key = True)

def connect_to_db(app):
        """Connects to Flask app"""
        db.app = app
        db.init_app(app)