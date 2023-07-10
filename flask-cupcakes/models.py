"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

DEF_IMG = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """A model for cupcakes"""
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, nullable = False, default = DEF_IMG)

    def to_dict(self):
        """Serialize the model to a dict"""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "image": self.image
        }


def connect_db(app):
    """Connects to database"""

    db.app = app
    db.init_app(app)