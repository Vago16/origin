from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.exceptions import Unauthorized

from models import db, connect_db, User, Feedback
from forms import Register, Login, FeedbackForm, Delete
from secret import APP_SECRET_KEY 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///flask-feedback"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
connect_db(app)

@app.route("/")
def homepage():
    """Homepage"""
    return redirect("/register")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    """Show a form that when submitted will register/create a user, """
    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = Register()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        
        user = User.register(username, password, email, first_name, last_name,)

        db.session.commit()
        session['username'] = user.username

        return redirect(f"/users/{user.username}")

    else:
        return render_template("users/register.html", form = form)
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    """Show a form that when submitted will login a user, then process, ensuring user is auntheticated"""
    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = Login()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)  # <User> or False
        if user:
            session['username'] = user.username
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors = ["Invalid username/password."]
            return render_template("users/login.html", form = form)

    return render_template("users/login.html", form = form)

@app.route("/users/<username>")
def show(username):
    ## """Secret"""
    ## if "user_id" not in session:
    ##     flash ("no")
    ##else:
    ##    render_template("secret.html")
    """Display a template the shows information about that user"""
    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username)
    form = Delete()

    return render_template("users/show.html", user = user, form = form)

@app.route("/logout")
def logout():
    """Shows a way to logout"""
    session.pop("username")
    return redirect("/login")

@app.route("/users/<username>/delete", methods=["POST"])
def remove_user(username):
    """Remove the user from the database"""
    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username)
    db.session.delete(user)
    db.session.commit()
    session.pop("username")

    return redirect("/login")

@app.route("/users/<username>/feedback/new", methods = ["GET", "POST"])
def new_feedback(username):
    """Show add-feedback form and process it."""

    if "username" not in session or username != session['username']:
        raise Unauthorized()

    form = FeedbackForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        feedback = Feedback(title = title, content = content, username = username)

        db.session.add(feedback)
        db.session.commit()

        return redirect(f"/users/{feedback.username}")

    else:
        return render_template("feedback/new.html", form = form)

@app.route("/feedback/<int:feedback_id>/update", methods = ["GET", "POST"])
def update_feedback(feedback_id):
    """Display a form to edit feedback"""
    feedback = Feedback.query.get(feedback_id)

    if "username" not in session or feedback.username != session['username']:
        raise Unauthorized()

    form = FeedbackForm(obj = feedback)

    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data

        db.session.commit()

        return redirect(f"/users/{feedback.username}")

    return render_template("/feedback/edit.html", form = form, feedback = feedback)


@app.route("/feedback/<int:feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    """Delete a specific piece of feedback and redirect to /users/<username>"""
    feedback = Feedback.query.get(feedback_id)
    if "username" not in session or feedback.username != session['username']:
        raise Unauthorized()

    form = Delete()

    if form.validate_on_submit():
        db.session.delete(feedback)
        db.session.commit()

    return redirect(f"/users/{feedback.username}")


