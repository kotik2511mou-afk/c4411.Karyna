import sqlite3

connection = sqlite3.connect("itstep_DBsi3",5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (neme) VALUES ('Karyna');")
cur.execute("INSERT INTO first_table (neme) VALUES ('Karina');")
connection.commit()
connection.close()