from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    """Model for users of the site"""
    __tablename__ = "users"
    username = db.Column(db.String(20), unique = True, primary_key = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    first_name = db.Column(db.Text(30), nullable = False)
    last_name = db.Column(db.Text(30), nullable = False)

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """Registers a user with relevant information and hashes their password"""
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(username = username,
                   password = hashed_utf8,
                   email = email,
                   first_name = first_name,
                   last_name = last_name)
        db.session.add(user)
        
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        """Makes sure username is in database and that password given is correct"""
        user = User.query.filter_by(username = username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False
        
class Feedback(db.model):
    """Feedback"""
    __tablename__ = "feedback"

    id = db.Column(primary_key = True, nullable = False)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    username = db.Column(db.String(20),
                         db.ForeignKey('users.username'),
                         nullable = False)

def connect_db(app):
    """Connect database to app"""
    db.app = app
    db.init_app(app)
