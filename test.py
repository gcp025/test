from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    try:
        body = request.get_json(force=True)  # ← force=True を追加！
        print("📦 Webhook受信内容：", body)

        user_id = body["events"][0]["source"]["userId"]
        print("✅ あなたの userId:", user_id)
    except Exception as e:
        print("⚠ エラー発生:", e)

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
