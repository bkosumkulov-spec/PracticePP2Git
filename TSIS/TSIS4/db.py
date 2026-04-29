# db.py — дерекқормен жұмыс
import psycopg2
from config import DB


def connect():
    try:
        return psycopg2.connect(**DB)
    except Exception as e:
        print("DB қосылмады:", e)
        return None


def init_db():
    conn = connect()
    if not conn:
        return False
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INTEGER REFERENCES players(id),
            score INTEGER NOT NULL,
            level_reached INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    conn.close()
    return True


def get_or_create_player(username):
    conn = connect()
    if not conn:
        return None
    cur = conn.cursor()
    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    row = cur.fetchone()
    if row:
        conn.close()
        return row[0]
    cur.execute("INSERT INTO players (username) VALUES (%s) RETURNING id", (username,))
    pid = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return pid


def save_session(player_id, score, level):
    conn = connect()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s,%s,%s)",
        (player_id, score, level)
    )
    conn.commit()
    conn.close()


def get_top10():
    conn = connect()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute("""
        SELECT p.username, gs.score, gs.level_reached,
               TO_CHAR(gs.played_at, 'YYYY-MM-DD')
        FROM game_sessions gs
        JOIN players p ON p.id = gs.player_id
        ORDER BY gs.score DESC LIMIT 10
    """)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_best(player_id):
    conn = connect()
    if not conn:
        return 0
    cur = conn.cursor()
    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id = %s", (player_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row and row[0] else 0