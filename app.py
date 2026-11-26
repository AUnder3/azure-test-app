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
    <html>
    <head>
        <title>MST Dashboard Proof of Concept</title>

        <style>
            body {{
                font-family: Segoe UI, Arial, sans-serif;
                margin: 40px;
                background-color: #f5f5f5;
            }}

            .card {{
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}

            h1 {{
                color: #0078D4;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
            }}

            th {{
                background-color: #0078D4;
                color: white;
                padding: 10px;
            }}

            td {{
                border: 1px solid #dddddd;
                padding: 10px;
            }}

            select {{
                padding: 8px;
                margin-bottom: 15px;
            }}

            .success {{
                color: green;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>

        <h1>MST Dashboard Proof of Concept</h1>

        <div class="card">
            <h2>Progress Achieved</h2>
            <ul>
                <li class="success">✓ Azure Web App deployed</li>
                <li class="success">✓ GitHub deployment pipeline working</li>
                <li class="success">✓ CSV data source connected</li>
                <li class="success">✓ Interactive filtering implemented</li>
                <li class="success">✓ Managed Identity authentication working</li>
            </ul>
        </div>

        <div class="card">
            <h2>MST Sample Results</h2>

            <form method="get">
                <label><strong>Site:</strong></label>

                <select name="site" onchange="this.form.submit()">
                    <option value="">All Sites</option>
                    {options}
                </select>
            </form>

            {df_filtered.to_html(index=False)}
        </div>

        <div class="card">
            <h2>Target Architecture</h2>

            <pre>
MicrobiologicalTools SharePoint
            ↓
MST Downloads CSV
            ↓
Microsoft Graph
            ↓
Managed Identity
            ↓
Azure Web App
            ↓
Interactive Dashboard
            </pre>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
