import sqlite3
from os import path

conn=sqlite3.connect("C://Python27/mycode/sample.db")
c = conn.cursor()
x = 'Carry','Chan',
c.execute('SELECT email, last, first FROM users where last=? or last=?',x)
for row in c.fetchall():
    print row[0], row[1], row[2]

c.execute('SELECT * from users')
for row in c.fetchall():
    print row[0]


conn.close()    
