from flask import Flask
from azure.identity import ManagedIdentityCredential
import requests

app = Flask(__name__)

@app.route("/")
def home():

    credential = ManagedIdentityCredential()

    token = credential.get_token(
        "https://graph.microsoft.com/.default"
    )

    headers = {
        "Authorization": f"Bearer {token.token}"
    }

    response = requests.get(
        "https://graph.microsoft.com/v1.0/sites?search=MicrobiologicalTools",
        headers=headers
    )

    return f"""
    <h1>Graph Test</h1>
    <pre>{response.status_code}</pre>
    <pre>{response.text}</pre>
    """

if __name__ == "__main__":
    app.run()
