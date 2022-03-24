import sqlite3

con = sqlite3.connect("hackathon22.db")
print("Database opened successfully")

con.execute("Create table HelpDetails(name TEXT, contact TEXT, address TEXT, state TEXT,pincode TEXT,areasize TEXT)")

con.execute("Create table SoilTest(name TEXT, contact TEXT,state TEXT,pincode TEXT,address TEXT)")

print("Table created successfully")

con.close()