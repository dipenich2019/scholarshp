import sqlite3

conn = sqlite3.connect('sqlite3_database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE students (student_id   INT ,name TEXT, addr TEXT, city TEXT, pin TEXT)')
print ("Table created successfully")
conn.close()


conn.execute('CREATE TABLE Present(ID  INT ,GIFT   TEXT, DESCRIPTION   TEXT)')




print ("Table Present created successfully")
conn.close()

 