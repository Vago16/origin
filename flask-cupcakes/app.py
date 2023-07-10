"""Flask app for Cupcakes"""
from models import Cupcake, db, connect_db
from flask import Flask, jsonify, request, render_template
from secret import APP_SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def root():
    """Root page"""
    return render_template("index.html")

@app.route("api/cupcakes")
def cupcake_list():
    """Get data about all cupcakes"""
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = cupcakes)

@app.route("api/cupcakes/<int:cupcake_id>")
def cupcake_show(cupcake_id):
    """Get data about one specific cupcake by its ID"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes", methods = ["POST"])
def cupcake_create():
    """Create a cupcake with flavor, size, rating and image data from the body of the request"""
    data = request.json

    cupcake = Cupcake(flavor = data['flavor'],
                      rating = data['rating'],
                      size = data['size'],
                      image = data['image'] or None)
    
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake = cupcake.to_dict()), 201)

@app.route("api/cupcakes/<cupcake_id>", methods = ["PATCH"])
def cupcake_update(cupcake_id):
    """Update a cupcake with the id passed in the URL and flavor, size, 
    rating and image data from the body of the request."""
    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor'],
    cupcake.rating = data['rating'], 
    cupcake.size = data['size'],
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake = cupcake.to_dict()))

@app.route("/api/cupcake/<cupcake_id>", methods = ["DELETE"])
def cupcake_delete(cupcake_id):
    """Deletes a cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit

    return jsonify(message = "Deleted")




