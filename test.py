from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    print("🚀 Webhook Hit!")
    print("📬 Headers:", dict(request.headers))
    print("📦 Raw Data:", request.data)

    try:
        body = request.get_json(force=True)
        print("📦 JSON Body:", body)
        user_id = body["events"][0]["source"]["userId"]
        print("✅ あなたの userId:", user_id)
    except Exception as e:
        print("⚠ エラー:", e)

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
