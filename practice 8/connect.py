import psycopg2
from config import load_config

def connect():
    config = load_config()
    try:
        conn = psycopg2.connect(**config)
        return conn
    except Exception as e:
        print("Connection error:", e)
        return None