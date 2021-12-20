from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = 'ea2b8e9c0be7486719441667a3bea3799da2d1910e28c9760447f33b52456a20'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# login module
login_manager = LoginManager()
login_manager.init_app(app)


## CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# # creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # generate new User class
        new_user = User()
        new_user.email = request.form.get("email")
        new_user.password = generate_password_hash(request.form.get("password"))
        new_user.name = request.form.get("name")
        if User.query.filter_by(email=new_user.email).first():
            flash("You've already signed up with that email, please log in instead.")
            return redirect(url_for("login"))
        db.session.add(new_user)
        db.session.commit()
        # log in new user
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        # check user exists and password is correct
        if not user:
            flash("Email doesn't exist. Please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash("Wrong password. Please try again.")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html")


@app.route('/secrets/')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory("static", "files/cheat_sheet.pdf")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
