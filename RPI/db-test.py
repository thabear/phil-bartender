import sqlite3

conn = sqlite3.connect('phil.db')
curs = conn.cursor()

print ("\n DB Shit:\n")
curs.execute("SELECT SUM(dc.cost) FROM drinkSales AS ds, drinkConfig AS dc WHERE ds.drinkName = dc.drinkName;")
print (curs.fetchall())
conn.close()
# for row in curs.execute("SELECT * FROM drinkSales;"):
#   print row
