import sqlite3
def song_db():
    con = sqlite3.connect("songs.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS songs (
        path TEXT NOT NULL UNIQUE,
        title TEXT NOT NULL,
        artist TEXT NOT NULL,
        album TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    """)

    con.commit()
    con.close()

