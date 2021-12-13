from flask import Flask, render_template
import requests

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)

response = requests.get(BLOG_URL)
blog_data = response.json()

posts = {}
for blog in blog_data:
    postid = blog['id']
    title = blog['title']
    body = blog['body']
    posts[postid] = {
        "title": title,
        "body": body,
    }


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_data)


@app.route('/post/<blog_id>')
def post(blog_id):
    post_content = posts[int(blog_id)]
    return render_template("post.html", contents=post_content)


if __name__ == "__main__":
    app.run(debug=True)
