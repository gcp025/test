from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    body = request.json
    print("📦 Webhook受信内容：", body)  # ← ここ追加！

    try:
        user_id = body["events"][0]["source"]["userId"]
        print("✅ あなたの userId:", user_id)
    except Exception as e:
        print("⚠ エラー:", e)

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
