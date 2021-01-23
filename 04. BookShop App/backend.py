import sqlite3

def connect():
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookdata (id INTEGER PRIMARY KEY, title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def view_all():
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookdata")
    rows = cur.fetchall()
    conn.close()   
    return rows

def add_book(title, author, year, isbn):
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO bookdata VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close() 

def search_book(title='', author='', year='', isbn=''):
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookdata WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_entry(id):
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM bookdata WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_book(id, title, author, year, isbn):
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute("UPDATE bookdata SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()