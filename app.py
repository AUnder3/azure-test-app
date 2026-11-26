from flask import Flask
from azure.identity import ManagedIdentityCredential

app = Flask(__name__)

@app.route("/")
def home():

    try:

        credential = ManagedIdentityCredential()

        token = credential.get_token(
            "https://graph.microsoft.com/.default"
        )

        return f"""
        <h1>Managed Identity Test</h1>
        <p>Success ✅</p>
        <p>Token obtained successfully.</p>
        """

    except Exception as e:

        return f"""
        <h1>Managed Identity Test</h1>
        <p>Failed ❌</p>
        <pre>{str(e)}</pre>
        """

if __name__ == "__main__":
    app.run()
