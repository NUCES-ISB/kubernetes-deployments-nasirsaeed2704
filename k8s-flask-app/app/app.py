from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App is Running!"

@app.route('/db')
def check_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port="5432"
        )
        return "Database connected successfully!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
