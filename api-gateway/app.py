from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://backend:5001/process')
    return jsonify({"message": "Gateway received", "backend_response": response.json()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
