import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Saicharan88@'
)

cur = conn.cursor()

class read():

    def departmentread(x):
        cur.execute("select * from department")
        print(cur.fetchall())
       

    def courseread(x):
        cur.execute("select * from course")
        cur.fetchall()

    def facultyread(x):
        cur.execute("select * from faculty")
        cur.fetchall()

    def studentread(x):
        cur.execute("select * from student")
        cur.fetchall()