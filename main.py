from flask import Flask, request
import os
import requests

app = Flask(__name__)

LINE_TOKEN = "あなたのチャネルアクセストークン"  # 必ず設定！
TXT_PATH = "Mito_garbage_2025.txt"

def find_garbage_info(date_text):
    with open(TXT_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # "8/7" で始まる行を探す
    for line in lines:
        if line.startswith(date_text):
            return line.strip()
    return None

@app.route("/", methods=["POST"])
def webhook():
    body = request.get_json(force=True)
    print("🔥 POST / HIT", flush=True)
    print("📦 JSON Body:", body, flush=True)

    try:
        event = body["events"][0]
        reply_token = event["replyToken"]
        user_message = event["message"]["text"].strip()  # 例: "8/7"

        print("💬 ユーザーのメッセージ:", user_message, flush=True)

        # 入力が「m/d」形式かチェック
        if "/" in user_message:
            garbage_info = find_garbage_info(user_message)
            if garbage_info:
                reply_text = f"🧹 ごみ収集情報：\n{garbage_info}"
            else:
                reply_text = f"⚠️ {user_message} の収集データは見つかりません"
        else:
            reply_text = "📅 日付は例: 8/7 のように送ってね！"

        # LINEに返信
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {LINE_TOKEN}"
        }
        payload = {
            "replyToken": reply_token,
            "messages": [
                {
                    "type": "text",
                    "text": reply_text
                }
            ]
        }
        res = requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=payload)
        print("📨 返信結果:", res.status_code, res.text, flush=True)

    except Exception as e:
        print("⚠️ エラー:", e, flush=True)

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Flask起動 on port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
