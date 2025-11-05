import sqlite3
def initialize_db():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT NOT NULL UNIQUE,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        admin TEXT DEFAULT '0'
    )
    """)

    con.commit()
    con.close()

