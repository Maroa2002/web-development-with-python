from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("index.html", posts=blog_data)


@app.route("/blog/<int:num>")
def get_blog(num):
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("post.html", posts=blog_data, number=num)


if __name__ == "__main__":
    app.run(debug=True)
