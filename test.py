from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    print("🔥 POST / HIT")
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 起動中 on port {port}")
    app.run(host="0.0.0.0", port=port)
