from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello Ashley!</h1>
    <p>My first Azure web app using GitHub!</p>
    """
