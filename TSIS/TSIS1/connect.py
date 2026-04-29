import psycopg2
from config import load_config
import os

def connect():
    try:
        config = load_config()
        # Фикс кодировки для Windows
        os.environ['PGCLIENTENCODING'] = 'utf8'
        conn = psycopg2.connect(**config)
        print("Connected to PostgreSQL!")
        return conn
    except Exception as e:
        print("Error:", e)
