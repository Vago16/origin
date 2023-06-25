"""Blogly application."""

from flask import Flask, redirect, request, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def root():
    """Redirect to list of users. (We will fix this in a later step)."""
    return redirect("/users")

@app.route('/users')
def users_index():
    """Show all users."""
    users = User.query.order_by(User.first_name, User.last_name).all()
    return render_template('users/index.html', users = users)

@app.route('/users/new', methods = ["GET"])
def user_form():
    """Show an add form for users"""
    return render_template('users/new.html')


@app.route('/users/new', methods = ["POST"])
def user_add():
    """Process the add form, adding a new user and going back to /users"""
    new_user = User(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        image_url = request.form['image_url'] or None
    )

@app.route('/users/<int:user_id>')
def users_show(user_id):
    """Show information about the given user.
        Have a button to get to their edit page, and to delete the user."""
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user = user)

@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """Show the edit page for a user.
    Have a cancel button that returns to the detail page for a user, and a save button that updates the user."""
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods = ["POST"])
def users_edit_post(user_id):
    """Process the edit form, returning the user to the /users page."""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()
    return redirect("/users")

@app.route('/users/<int:user_id>/delete', methods = ["POST"])
def users_delete(user_id):
    """Delete the user."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect ("/users")