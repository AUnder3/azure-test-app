from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    df = pd.read_csv("results.csv")

    site = request.args.get("site", "")

    if site:
        df_filtered = df[df["Site"] == site]
    else:
        df_filtered = df

    options = ""

    for s in df["Site"].unique():
        selected = "selected" if s == site else ""
        options += f'<option value="{s}" {selected}>{s}</option>'

    return f"""
    <h1>Bathing Water Results</h1>

    <form method="get">
        <select name="site">
            <option value="">All Sites</option>
            {options}
        </select>
        <input type="submit" value="Filter">
    </form>

    <br>

    {df_filtered.to_html(index=False)}
    """
