from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])

ULTRAVOX_API_KEY = os.getenv("ULTRAVOX_API_KEY")
AGENT_ID = os.getenv("ULTRAVOX_AGENT_ID")

if not ULTRAVOX_API_KEY or not AGENT_ID:
    raise ValueError("❌ Missing ULTRAVOX_API_KEY or ULTRAVOX_AGENT_ID in .env")

@app.route("/create-call", methods=["POST"])
def create_call():
    """Create a new call using the Ultravox API"""
    url = f"https://api.ultravox.ai/api/agents/{AGENT_ID}/calls"

    headers = {
        "Content-Type": "application/json",
        "X-API-Key": ULTRAVOX_API_KEY
    }

    payload = {
        "metadata": {},
        "medium": {"webRtc": {}}
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    data = response.json()
    return jsonify({
        "callId": data.get("id"),
        "joinUrl": data.get("joinUrl")
    }), 201

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Ultravox Flask API running"}), 200
