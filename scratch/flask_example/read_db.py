import sqlite3

con = sqlite3.connect('data.db')

cur = con.cursor()

res = cur.execute("SELECT * FROM form_entries")


for row in res:
    print(row)
