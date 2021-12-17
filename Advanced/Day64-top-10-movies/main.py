from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests
import os

# API
TMDB_SEARCH = "https://api.themoviedb.org/3/search/movie"
TMDB_FIND_ID = "https://api.themoviedb.org/3/movie"
TMDB_KEY = os.environ["TMDB_KEY"]


# -------------------------APP setup ------------------------------- #
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# -------------------------DB setup ------------------------------- #
# Create db using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies-collection.db'
# handle the warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


# # create the table
# db.create_all()
# db.session.commit()

# ------------------------- Forms ------------------------------- #
class UpdateForm(FlaskForm):
    rating = FloatField(
        label="Your Rating out of 10, e.g. 7.5",
        validators=[DataRequired()]
    )
    review = StringField(
        label="Your Review",
        validators=[DataRequired(), Length(max=250)]
    )
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField(
        label="Movie Title",
        validators=[DataRequired()]
    )
    submit = SubmitField('Add Movie')


# ------------------------- Website setup ------------------------------- #
@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by("rating").all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = UpdateForm()
    movie_id = request.args.get("id")
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = request.form.get("rating")
        movie_to_update.review = request.form.get("review")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_to_update, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        new_movie = request.form.get("title")
        params = {
            "api_key": TMDB_KEY,
            "query": new_movie
        }
        response = requests.get(TMDB_SEARCH, params=params)
        movies_data = response.json()["results"]
        return render_template("select.html", results=movies_data)
    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select():
    movie_id = request.args.get("id")
    params = {
        "api_key": TMDB_KEY,
    }
    response = requests.get(f"{TMDB_FIND_ID}/{movie_id}", params=params)
    movie_data = response.json()
    new_movie = Movie(
        title=movie_data["original_title"],
        year=movie_data["release_date"].split("-")[0],
        description=movie_data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    movie_to_update = Movie.query.filter_by(title=movie_data["title"]).first()
    return redirect(url_for("edit", id=movie_to_update.id))


if __name__ == '__main__':
    app.run(debug=True)
