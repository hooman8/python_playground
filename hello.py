from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = "Nina"
    return render_template("index.html", name=name)


@app.route("/name/<name>")
def hello_name(name):
    return f"hello, {name}"


if __name__ == "__main__":
    app.run(debug=True)


# FLASK_APP=hello.py flask run
# FLASK_APP=hello.py FLASK_ENV=development flask run
