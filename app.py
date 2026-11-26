from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    site = request.args.get("site")

    df = pd.read_csv("results.csv")

    if site:
        df = df[df["Site"] == site]

    return f"""
    <h1>Bathing Water Results</h1>
    {df.to_html(index=False)}
    """

if __name__ == "__main__":
    app.run()
