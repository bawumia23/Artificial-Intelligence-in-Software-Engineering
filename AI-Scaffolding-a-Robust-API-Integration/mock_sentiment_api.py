#!/usr/bin/python3
"""A tiny local stand-in for api.text-processing.com, for demo purposes."""
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/sentiment/', methods=['POST'])
def sentiment():
    """Return a canned positive sentiment label, checking for the header."""
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return jsonify({"error": "missing API key"}), 401
    return jsonify({"label": "pos", "probability": {"pos": 0.9, "neg": 0.1}})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
