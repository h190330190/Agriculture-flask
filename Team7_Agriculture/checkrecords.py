import sqlite3

con = sqlite3.connect("hackathon22.db")
cur = con.cursor()
cur.execute("select * from HelpDetails")
rows = cur.fetchall()
for i in rows:
    print (i)
