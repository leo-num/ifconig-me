from flask import Flask, make_response
import json
import sqlite3

app = Flask(__name__)

DATABASE = "counter.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS hits (id INTEGER PRIMARY KEY, count INTEGER)")
    cursor.execute("INSERT OR IGNORE INTO hits (id, count) VALUES (1, 0)")
    conn.commit()
    conn.close()

def increment_and_get_hits():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE hits SET count = count + 1 WHERE id = 1")
    conn.commit()
    cursor.execute("SELECT count FROM hits WHERE id = 1")
    count = cursor.fetchone()[0]
    conn.close()
    return count

@app.route("/")
def home():
    hits = increment_and_get_hits()
    message = f"You spelled it wrong ☺️. This has happened {hits} times this year. Take care!"
    return message, 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)