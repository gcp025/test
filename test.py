from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    body = request.json
    try:
        user_id = body["events"][0]["source"]["userId"]
        print("✅ あなたの userId：", user_id)
    except Exception as e:
        print("⚠ エラー:", e)
    return "OK", 200
