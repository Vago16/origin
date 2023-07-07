from flask import Flask, url_for, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import Pet, db, connect_db
from forms import AddPet, EditPet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()
app.run()

toolbar = DebugToolbarExtension(app)

@app.route("/")
def pet_list():
    """List of all pets"""
    pets = Pet.query.all()
    return render_template("pet_list.html", pets = pets)

@app.route("/add", methods = ["GET", "POST"])
def add_pet():
    """Create a form for adding pets"""
    form = AddPet()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_of_pets'))
    
    else:
        return render_template("add_pet_form.html", form = form)
    
@app.route("/<int:pet_id>", methods = ["GET", "POST"])
def edit_pet(pet_id):
    """Edits the pets"""
    pet = Pet.query.get_or_404(pet_id)
    form =EditPet(obj = pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} has been updated.")
        return redirect(url_for('list_of_pets'))
    
    else:
        return render_template("edit_pet_form.html", pet = pet, form = form)
    
