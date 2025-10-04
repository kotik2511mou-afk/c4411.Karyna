import sqlite3

connection = sqlite3.connect("itstep_DBsi3",5)
cur = connection.cursor()
cur.execute("SELECT rowid,neme first_table;")
connection.commit()

connection.close()