from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    return "Postback bot is running"

@app.route("/postback")
def postback():
    payout = request.args.get("payout", "0")
    status = request.args.get("status", "unknown")
    subid = request.args.get("subid", "no_subid")

    text = f"""
🔥 Нова конверсія!

Status: {status}
Payout: {payout}$
SubID: {subid}
"""

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )

    return "OK"
    if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
