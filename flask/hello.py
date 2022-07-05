from flask import Flask
import time

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        time.sleep(5)
        function()
    return wrapper_function


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/username/<int:name>")
@make_bold
def bye(name):
    return f"hey {name} get out"


if __name__ == "__main__":
    app.run(debug=True)