from flask import Flask, render_template
import requests

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

# Set up the web
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:blog_id>')
def post(blog_id):
    return render_template("post.html", blog=ref_blog[blog_id])


if __name__ == "__main__":
    app.run(debug=True)
