from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    df = pd.read_csv("results.csv")

   return f"""
<h1>Bathing Water Results</h1>
{df.to_html(index=False)}
"""
