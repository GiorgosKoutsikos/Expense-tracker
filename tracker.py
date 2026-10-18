import sqlite3


def init_db():
    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("""
                  CREATE TABLE IF NOT EXISTS expenses (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  description TEXT,
                  amount REAL)
    """)

    conn.commit()
    conn.close()


def add_expense(description, amount):
    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO expenses (description, amount) VALUES (?, ?)", (description, amount))

    conn.commit()
    conn.close()


n = init_db()
k = add_expense("coffee", 2.50)
print(n, k)
