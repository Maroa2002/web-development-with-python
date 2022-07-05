from flask import Flask, render_template
import requests

app = Flask(__name__)

api = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=api)
data = response.json()


@app.route("/")
def home():
    return render_template("index.html", blogs=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def post(num):
    return render_template("post.html", blogs=data, num=num)


if __name__ == "__main__":
    app.run(debug=True)
