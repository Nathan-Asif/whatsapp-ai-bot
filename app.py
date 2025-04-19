from flask import Flask, request, jsonify
import requests
import os
from utils import geminiModel
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

@app.route("/bg-webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Verification failed", 403

    if request.method == "POST":
        data = request.get_json()
        print(data)

        try:
            user_msg = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

            ai_response = geminiModel(user_msg)

            print(f"User: {user_msg}")
            print(f"Bot: {ai_response}")
        except Exception as e:
            print("Error:", e)

        return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)