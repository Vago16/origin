"""Blogly application."""

from flask import Flask, redirect, request, render_template, flash
from models import db, connect_db, User, Post, Tag, PostTag
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all

@app.route('/')
def root():
    """Shows list of 5 most recent posts"""
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template("homepage.html", posts = posts)

@app.errorhandler(404)
def page_not_found(error):
    """Shows a 404 page not found"""
    return render_template("404_page.html"), 404

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

    db.session.add(new_user)
    db.session.commit()
    flash(f"User {new_user.full_name} has been added")

    return redirect ("/users")

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
    return render_template('users/edit.html', user = user)

@app.route('/users/<int:user_id>/edit', methods = ["POST"])
def users_edit_post(user_id):
    """Process the edit form, returning the user to the /users page."""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()
    flash(f"User {user.full_name} has been edited")

    return redirect("/users")

@app.route('/users/<int:user_id>/delete', methods = ["POST"])
def users_delete(user_id):
    """Delete the user."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f"User {user.full_name} has been deleted")
    return redirect ("/users")

## Add Post Routes ##

@app.route('/users/<int:user_id>/posts/new')
def new_post_form(user_id):
    """Show form to add a post for that user"""
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template('posts/new.html', user = user, tags = tags)

@app.route('/users/<int:user_id>/posts/new', methods = ["POST"])
def new_post(user_id):
    """Handle add form; add post and redirect to the user detail page."""
    user = User.query.get_or_404(user_id)
    tag_ids= [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    new_post = Post(title=request.form['title'], content=request.form['content'], user = user, tags = tags)


    db.session.add(new_post)
    db.session.commit()
    flash(f"Post '{new_post.title}' has been added")

    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Show a post. Show buttons to edit and delete the post."""
    post = Post.query.get_or_404(post_id)
    return render_template('posts/show.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """Show form to edit a post, and to cancel (back to user page)."""
    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    return render_template('posts/edit.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods = ["POST"])
def handle_edit_post(post_id):
    """Handle editing of a post. Redirect back to the post view."""
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    db.session.add(post)
    db.session.commit()
    flash(f"Post '{post.title}' has been edited.")
    return redirect(f"/users/{post.user_id}")

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """Delete the post."""
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post.title}has been deleted.")

    return redirect(f"/users/{post.user_id}")

## Add Tag Routes ##

@app.route('/tags')
def tags_index():
    """Lists all tags, with links to the tag detail page."""
    tags = Tag.query.all()
    return render_template('tags/index.html', tags = tags)

@app.route('/tags/<int:tag_id>')
def show_tags(tag_id):
    """Show detail about a tag. Have links to edit form and to delete."""
    tag = Tag.query.getor_404(tag_id)
    return render_template('tags/show.html', tag = tag)

@app.route('/tags/new')
def tags_new():
    """Shows a form to add a new tag."""
    post = Post.query.all()
    return render_template('tags/new.html', post = post)

@app.route('/tags/new', methods = ["POST"])
def tag_form():
    """Process add form, adds tag, and redirect to tag list."""
    post_ids = [int(num) for num in request.form.getlist("posts")]
    posts = Post.query.filter(Post.id.in_(post_ids)).all()
    new_tag = Tag(name=request.form['name'], posts=posts)

    db.session.add(new_tag)
    db.session.commit()

    flash(f"The tag '{new_tag.name}' has been added to your post.")

    return redirect("/tags")

@app.route('/tags/<int:tag_id>/edit')
def edit_tag(tag_id):
    """Show edit form for a tag."""
    tag = Tag.query.get_or_404(tag_id)
    posts = Post.query.all()
    return render_template('tags/edit.html', tag = tag, posts = posts)

@app.route('/tags/<int:tag_id>/edit', methods =["POST"])
def edit_tag_post(tag_id):
    """Process edit form, edit tag, and redirects to the tags list."""
    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['name']
    post_ids = [int(num) for num in request.form.getlist("posts")]
    tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

    db.session.add(tag)
    db.session.commit()

    flash(f"The tag '{tag.name}' has been edited.")

    return redirect("/tags")

@app.route('/tags/<int:tag_id>/delete', methods = ["POST"])
def delete_tag(tag_id):
    """Deletes a tag"""
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()

    flash(f"The tag '{tag.name}' has been deleted.")

    return redirect("/tags")
