import sqlite3

conn = sqlite3.connect('rps_data.db')

print ("Opened database successfully")


cursor = conn.execute('SELECT * FROM standings')
for row in cursor:
    print(row)