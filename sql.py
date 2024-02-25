import sqlite3

connection = sqlite3.connect("Dvoechniki.sl3", 5)
cur = connection.cursor()

# cur.execute("UPDATE srezi SET name = 'Name' WHERE rowid = 1;")
# cur.execute("SELECT * FROM srezi")
# cur.execute("INSERT INTO srezi (name) VALUES ('Mikella');")

res = cur.fetchall()
print(res)

connection.commit()
connection.close()