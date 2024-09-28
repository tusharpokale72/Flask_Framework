import sqlite3

conn = sqlite3.connect('database4.db')
print("Open Database Successfully...!!")

conn.execute('CREATE TABLE students_4 (name TEXT, addr TEXT, city TEXT, pin TEXT )')
print("Table created Successfully...!!")
conn.close()