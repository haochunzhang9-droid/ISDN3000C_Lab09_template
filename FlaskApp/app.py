import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    messages = conn.execute("SELECT * FROM messages ORDER BY created_at DESC").fetchall()
    conn.close()
    return render_template("index.html", messages=messages)

@app.route("/api/messages", methods=["POST"])
def add_message_api():
    data = request.get_json()
    name = data.get("name")
    message = data.get("message")

    if not name or not message:
        return jsonify({"status": "error", "message": "Name and message are required."}), 400

    if len(message) > 140:
        return jsonify({"status": "error", "message": "Message too long (max 140 characters)."}), 400

    conn = get_db_connection()
    conn.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Message added!"})


@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
