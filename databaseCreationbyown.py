import sqlite3

#connection to sqlite 
#connection object
connection_obj = sqlite3.connect('arc.db')
#cursor object 
cursor_obj = connection_obj.cursor()
#drop the t1 table if already exists

cursor_obj.execute("Drop table if exists t2")
#Creating table
table = '''CREATE TABLE t2(
    name varchar(34),
    class varchar(34),
    section varchar(34)
);
'''
connection_obj.execute(table)
connection_obj.execute('''
INSERT INTO t2 values("Abhishek", "Btech", "k32el")
''')
connection_obj.execute('''
INSERT INTO t2 values("Sonam", "Mtch", "m32el")
''')
connection_obj.execute('''
INSERT INTO t2 values("Chandu", "Pharmacy", "p32el")
''')
connection_obj.execute('''
INSERT INTO t2 values("Raja", "BA", "b32el")
''')
connection_obj.execute('''
INSERT INTO t2 values("Madhu", "Ma", "a32el")
''')
connection_obj.execute('''
INSERT INTO t2 values("Abhishek", "Ma", "a32el")
''')

# statement = """select * from t2"""
statement = '''select * from t2 where name = "Abhishek"'''
cursor_obj.execute(statement)
print("All the data")

#for fetching only one tuples
# output = cursor_obj.fetchone()
output = cursor_obj.fetchall()
for row in output:
    print(row)