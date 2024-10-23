# SQLlite->database: in-built in python for all the vatious 2-5 ownwards.
#rule:
'''
1.import sqlite3
2.Built up connection with database
3.generate cursor
*sql.db is default database
sqliteConnection = sqlite3.connect('sql.db')
datatype in sqlite:
NUll, real, integer, text, BLOB(python bytes)
'''
import sqlite3
#connect to DB and create a cursor
sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()
print('DB Init')

#write a query and execute it with cursor
query = 'Select sqlite_version();'
cursor.execute(query)

#fetch and output result
result = cursor.fetchall()
print('SQLite Version is {}'.format(result))

#close the cursor
cursor.close()

#close DB Connection
sqliteConnection.close()
print('SQLite connection closed')
