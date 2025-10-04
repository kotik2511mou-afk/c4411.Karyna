import sqlite3

connection = sqlite3.connect("itstep_DBsi3",5)
cur = connection.cursor()
cur.execute("CREATE TABLE first_table(neme TEXT);")
connection.commit()
connection.close()