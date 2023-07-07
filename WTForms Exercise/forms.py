from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField
from wtforms.validators import Optional, Length, URL, InputRequired, NumberRange

class AddPet(FlaskForm):
    """A form for adding pets"""
    name = StringField("Pet Name", validators = [InputRequired()])
    species = SelectField("Species", choices = [("cat", "Cat"), ("dog", "Dog")])
    photo_url = StringField("URL for Photo", validators = [URL(), Optional()])
    age = IntegerField("Age is Just a Number", validators = [NumberRange(min = 0, max = 30), Optional()])
    notes = TextAreaField("Notes", validators = [Length(min = 5), Optional()])

class EditPet(FlaskForm):
    """A form for editing pets"""
    photo_url = StringField("URL for Photo", validators = [URL(), Optional()])
    notes = TextAreaField("Notes", validators = [Length(min = 5), Optional()])
    available = BooleanField("Avialable?")