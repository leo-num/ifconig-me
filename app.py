from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Initialize database
DATABASE = "counter.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS hits (id INTEGER PRIMARY KEY, count INTEGER)")
    cursor.execute("INSERT OR IGNORE INTO hits (id, count) VALUES (1, 0)")
    conn.commit()
    conn.close()

# Increment counter and fetch the current count
def increment_and_get_hits():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE hits SET count = count + 1 WHERE id = 1")
    conn.commit()
    cursor.execute("SELECT count FROM hits WHERE id = 1")
    count = cursor.fetchone()[0]
    conn.close()
    return count

# Routes
@app.route("/")
def home():
    hits = increment_and_get_hits()
    message = {
        "message": "You spelled it wrong ☺️.",
        "hits": hits,
        "note": "Take care!"
    }
    return jsonify(message)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)