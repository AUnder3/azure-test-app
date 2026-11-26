from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Bathing Water Dashboard</h1>
    <ul>
        <li>Shrewsbury</li>
        <li>Ironbridge</li>
        <li>Ludlow</li>
    </ul>
    """
