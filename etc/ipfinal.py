import mysql.connector as my
con = my.connect(host="localhost", user="root", password="root12345", database="burhan")
cur = con.cursor()
cur.execute('select *from student where rn > 500;')
data = cur.fetchall()
for a in data:
    print(*a)