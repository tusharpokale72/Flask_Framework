import sqlite3

conn = sqlite3.connect('database_3.db')
print('Database created succesfully...!')

conn.execute('CREATE TABLE Students_3(name TEXT,addr Text,city TEXT,pin TEXT)')
print('Table created successfully...!!')
conn.close()