import sqlite3

#connection to sqlite 
#connection object
connection_obj = sqlite3.connect('arc.db')
#cursor object 
cursor_obj = connection_obj.cursor()
#drop the t1 table if already exists

cursor_obj.execute("Drop table if exists t1")
#Creating table
table = '''
CREATE TABLE t1(
    Email varchar(34) NOT NULL,
    First_Name char(34) NOT NULL,
    Last_Name Char(45),
    Score int
);
'''

cursor_obj.execute(table)

connection_obj.execute('''
INSERT INTO t1 values ("Abhishek@gamil.com", "Abhishek", "Gupta", 99)
''')
connection_obj.execute('''
INSERT INTO t1 values ("Rohan@gamil.com", "Rohan", "Gupta", 79)
''')
connection_obj.execute('''
INSERT INTO t1 values ("vishwjeet@gamil.com", "vishwjeet", "Singh", 59)
''')
connection_obj.execute('''
INSERT INTO t1 values ("komal@gamil.com", "Komal", "Sharma", 67)
''')
connection_obj.execute('''
INSERT INTO t1 values ("Manish@gamil.com", "Manish", "Agarwal", 99)
''')
connection_obj.execute('''
INSERT INTO t1 values ("sunidhi@gamil.com", "Sunidhi", "Chouhan", 99)
''')
statement = '''SELECT * FROM t1'''
cursor_obj.execute(statement)
print("All the data")
output = cursor_obj.fetchall()
for row in output:
    print(row)