from flask import Flask, request, jsonify, send_from_directory, render_template
from AuthenticationCheck.authentication import authenticate
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    api_key = data.get('api_key')

    if not api_key:
        return jsonify({"error": "API key is required"}), 400

    is_authenticated = authenticate(api_key)

    if is_authenticated:
        return jsonify({"message": "API key is valid"}), 200
    else:
        return jsonify({"error": "Invalid API key"}), 401

if __name__ == '__main__':
    app.run(debug=True)
