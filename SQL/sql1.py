import sqlite3 as sql

db = sql.connect(r"C:\Users\vektorel\Documents\GitHub\Python10\SQL\chinook.db")
cur = db.cursor()
cur.execute("SELECT * from albums")
liste =  cur.fetchall()
print(liste)
