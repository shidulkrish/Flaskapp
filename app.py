import os
from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route("/")
def index():
  try:
    conn = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "secret"),
        database=os.environ.get("DB_NAME", "testdb"),
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    db_time = cursor.fetchone()
    conn.close()
    return f"Connected to MySQL successfully! Database Server Time: {db_time[0]}"
  except Exception as e:
    return f"Database connection failed: {e}"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
