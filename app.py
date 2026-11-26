from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>Water Quality Dashboard</h1>
<p>Testing Azure deployment.</p>
<p>Site count: 25</p>
"""
