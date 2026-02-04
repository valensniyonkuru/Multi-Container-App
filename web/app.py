from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host=os.environ.get('DB_HOST', 'db'),
                user=os.environ.get('DB_USER', 'user'),
                password=os.environ.get('DB_PASSWORD', 'password'),
                database=os.environ.get('DB_NAME', 'testdb')
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Error connecting to DB: {err}")
            retries -= 1
            time.sleep(5)
    return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        if result:
            return f"Message from DB: {result[0]}"
        return "Connected to DB, but no message found."
    return "Failed to connect to database."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
