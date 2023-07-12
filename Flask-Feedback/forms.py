from wtforms import StringField, PasswordField
from wtforms.validators import Length, NumberRange, InputRequired, Optional, Email
from flask_wtf import FlaskForm

class Register(FlaskForm):
    """A form for registering new users"""
    username = StringField("Username",
        validators = [InputRequired(), Length(min = 6, max = 20)])
    password = PasswordField("Password",
        validators = [InputRequired(), Length(min = 6, max = 20)])
    email = StringField("Email",
        validators = [InputRequired(), Email(), Length(max = 35)])
    first_name = StringField("First Name",
        validators = [InputRequired(), Length(max = 15)])
    last_name = StringField("Last Name",
        validators = [InputRequired(), Length(max = 15)])
    
class Login(FlaskForm):
    """A form for logging in users"""
    username = StringField("Username",
        validators = [InputRequired(), Length(min = 6, max = 20)])
    password = PasswordField("Password",
        validators = [InputRequired(), Length(min = 6, max = 20)])
    
class FeedbackForm(FlaskForm):
    """A form to show all the feedback the user has given"""
    title = StringField("Title", validators = [Length(max = 50)])
    text = StringField("Text", validators = [InputRequired()])

class Delete(FlaskForm):
    """A form to delete user and erase all info from database"""