from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

# matched input
correct_email = "admin@email.com"
correct_pw = "12345678"


class LoginForm(FlaskForm):
    email = StringField(
        label="Email",
        validators=[DataRequired(), Length(min=8), Email(message="Invalid email address")]
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired()]
    )
    submit = SubmitField('Log in')


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app


app = create_app()
app.secret_key = "cndjsiciuae546daafe"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == correct_email and form.password.data == correct_pw:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
