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

def main():
    init_db()
    while True:
        print("----MENU----")
        print("1.Add")
        print("2.Details")
        print("3.Exit")
        print("\n")

        choice = input("Your choice: ")


        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
            print("\n")
        elif choice == "3":
            print("GoodBye!")
            break
        else:
            print("Not valid value.")

if __name__ == "__main__":
    main()
