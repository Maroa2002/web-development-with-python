from flask import Flask, render_template
import requests

app = Flask(__name__)
GENDERIZE_API = "https://api.genderize.io"
AGIFY_API = "https://api.agify.io"


@app.route("/")
def hello():
    return "Hello World"


@app.route("/guess/<username>")
def prediction(username):
    name_param = {
        "name": username
    }

    gender_response = requests.get(url=GENDERIZE_API, params=name_param)
    age_response = requests.get(url=AGIFY_API, params=name_param)

    gender_data = gender_response.json()
    age_data = age_response.json()
    return render_template("index.html", name=username.title(), gender=gender_data["gender"], age=age_data["age"])


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    render_template("blog.html", blog_posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)