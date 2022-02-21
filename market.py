from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    return "<h1>Home Page</h1>"


@app.route('/about/<username>')
def about_page(username):
    return f'<h1>About Page ({username})</h1>'
