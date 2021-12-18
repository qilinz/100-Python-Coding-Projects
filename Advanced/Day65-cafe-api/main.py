from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


## API setup
TopSecretKey = "bchwdbvcgwhlegv4562"


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all():
    all_cafes = db.session.query(Cafe).all()
    cafe_list = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafe=cafe_list)


@app.route("/search")
def search():
    location = request.args.get("location")
    cafe = Cafe.query.filter_by(location=location).first()
    print(cafe)
    if not cafe:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })
    return jsonify(cafe=cafe.to_dict())


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        has_sockets=bool(request.form.get("sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        response={
            "success": "Successfully added the new cafe."
        }
    )


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(
            response={
                "success": "Successfully updated the price."
            }
        ), 200
    return jsonify(
        error={
            "Not Found": "Sorry, we don't have a cafe with the given id."
        }
    ), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    user_key = request.args.get("api_key")
    if user_key != TopSecretKey:
        return jsonify(
            error={
                "Not Allowed": "Sorry, that's not allowed. Make sure you have the correct api_key."}
        ), 403
    cafe_to_delete = Cafe.query.get(cafe_id)
    if cafe_to_delete:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(
            response={
                "success": "Successfully deleted the cafe."
            }
        ), 200
    return jsonify(
        error={
            "Not Found": "Sorry, we don't have a cafe with the given id."
        }
    ), 404


if __name__ == '__main__':
    app.run(debug=True)
