import requests
import os
from flask import Flask, render_template, request

app = Flask(__name__)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:3000")

@app.route('/')
def index():
    try:
        response = requests.get(f"{BACKEND_URL}/api")
        data = response.json()
        return render_template('index.html', backend_message=data['message'])
    except Exception as e:
        return f"Error contacting backend: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

