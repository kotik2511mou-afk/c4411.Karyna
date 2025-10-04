import sqlite3

connection = sqlite3.connect("itstep_DBsi3",5)
cur = connection.cursor()
print(connection)
print(cur)
connection.close()