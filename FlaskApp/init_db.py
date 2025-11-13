import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")
    with open("schema.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database initialized: database.db")
