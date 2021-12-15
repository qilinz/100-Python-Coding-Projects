from flask import Flask, render_template, request
import requests
import smtplib
import os

# Get blog data
API_URL = "https://api.npoint.io/a501218628ba9f59a710"

response = requests.get(API_URL)
blogs_data = response.json()

# Frame the data
ref_blog = {}
for data in blogs_data:
    ref_blog[data["id"]] = {
        "title": data["title"],
        "subtitle": data["subtitle"],
        "body": data["body"],
    }


# Enable email sending
def send_email(username, email_address, phone_number, message):
    my_email = os.environ["GMAIL"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=os.environ["GMAIL_KEY"])
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: msg from personal website\n\n"
                f"Name:{username}\n"
                f"Email: {email_address}\n"
                f"Phone: {phone_number}\n"
                f"Message: {message}"
        )


# Set up the web
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    return render_template("post.html", blog=ref_blog[blog_id])


if __name__ == "__main__":
    app.run(debug=True)
