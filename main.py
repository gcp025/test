from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    print("🔥 POST / HIT", flush=True)
    try:
        body = request.get_json(force=True)
        print("📦 JSON Body:", body, flush=True)
        user_id = body["events"][0]["source"]["userId"]
        print("✅ あなたの userId:", user_id, flush=True)
    except Exception as e:
        print("⚠ エラー:", e, flush=True)
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Flask起動 on port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
