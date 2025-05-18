from flask import Flask
import requests
import os

app = Flask(__name__)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:3000")

@app.route('/')
def index():
    try:
        response = requests.get(f"{BACKEND_URL}/api")
        data = response.json()
        return f"<h1>{data['message']}</h1>"
    except:
        return "<h1>Could not reach backend</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

