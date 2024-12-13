import sqlite3
# connect to sqlite
connection = sqlite3.connect("Student.db")
# create a cursor to insert or retrieve the record from the Database
cursor = connection.cursor()
#Delete table if exists
delete_table = '''drop table  student''';
cursor.execute(delete_table)
# Create a Table : 
table_info = '''create table student(Name VARCHAR(25) , Class VARCHAR(25) , Section VARCHAR(25) , 
Marks INT)''';
# execute the cursor
cursor.execute(table_info)
#insert some records : 
cursor.execute('''Insert into student values('Krish','Data Science','A',90)''')
cursor.execute('''Insert into student values('Prabal','Data Science','A',96)''')
cursor.execute('''Insert into student values('Ankit','Data Analytics','B',65)''')
cursor.execute('''Insert into student values('Aman','Software Development','B',80)''')
cursor.execute('''Insert into student values('Kalyan','Cloud Computing','A',92)''')
cursor.execute('''Insert into student values('Ishant','GenAi','B',54)''')
#Display all the records
print(" The inserted records are :")
data = cursor.execute('''select * from student''')
for row in data :
    print(row)
#close the connection
connection.commit()
connection.close()
