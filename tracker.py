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


def add_expense():
    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    description = input("Description: ")
    amount = float(input("Price: "))

    cursor.execute("INSERT INTO expenses (description, amount) VALUES (?, ?)", (description, amount))

    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

init_db()
view_expenses()
