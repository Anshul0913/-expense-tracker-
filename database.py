import sqlite3

def connect ():
    conn= sqlite3.connect("expenss.db")  # create a database 
    return conn 

def create_table ():  # creating a table structure 
    conn = connect()
    cursor = conn.cursor () 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        item     TEXT NOT NULL,
        amount   REAL NOT NULL,
        category TEXT,
        date     TEXT NOT NULL
    )
""")
    
    conn.commit()
    conn.close()
    print("your Database is ready for use ")

def add_expense(item, amount, category, date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (item, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (item, amount, category, date))
    conn.commit()
    conn.close()
    print(f"Done! {item} - Rs.{amount} add ho gaya!")


def view_all ():
    conn= connect()
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM expenses  ORDER BY id")
    rows = cursor.fetchall () # gives data in a list 
    conn.close()
    return rows 

def total_spend():
    conn= connect()
    cursor= conn.cursor()
    cursor.execute("SELECT SUM (amount) FROM expenses ")
    total = cursor.fetchone()[0]
    conn.close()
    return total or 0 

def delete_expense(expense_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    print(f"Expense ID {expense_id} delete ho gaya!")


def filter_by_category(category):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    rows = cursor.fetchall()
    conn.close()
    return rows




    