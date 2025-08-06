from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])  # ← 必ず POST を明示！
def webhook():
    print("🔥 POST / HIT")
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
    print(f"🚀 Flask起動 on port {port}")
    app.run(host="0.0.0.0", port=port)
