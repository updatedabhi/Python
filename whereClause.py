import sqlite3

connection = sqlite3.connect('arc.db')
cursor = connection.cursor()

cursor.execute("Drop table if exists student")

table = '''
create table student(name varchar(34),
roll int,
section varchar(34));
'''
connection.execute(table)
connection.execute(
    '''insert into student values("Abhishek", 34, "B")'''
)
connection.execute(
    '''insert into student values("Sonu", 4, "B")'''
)
connection.execute(
    '''insert into student values("Radha", 3, "A")'''
)
connection.execute(
    '''insert into student values("Sean", 1, "A")'''
)
#where clause to retrive data
# cursor.execute("Select * from student where section = 'B'")
# cursor.execute("Select * from student where name like 'S%'")
# cursor.execute("select name from student order by name")
# cursor.execute("select * from student order by section")
#printing the cursor data
# print(cursor.fetchall())

# cursor.execute("update student SET name = 'Rohan' where roll > 3")
cursor.execute("delete from student where roll = 1")

print('\nafter updating')
print("Employee tale: ")
data = cursor.execute('''select * from student''')
for row in data:
    print(row)
connection.commit()
connection.close()
