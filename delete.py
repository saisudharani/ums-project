import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Saicharan88@'
)

cur = conn.cursor()

class deleted:

    def deptdelete(x,colname,id):
        cur.execute(f"delete from department where {colname}={id}")
        conn.commit()

    def crdelete(x,columnname,id):
        cur.execute(f"delete from course where {columnname}={id}")
        conn.commit()

    def fcdelete(x,columnname,id):
        cur.execute(f"delete from faculty where {columnname}={id}")
        conn.commit()

    def stdelete(x,columnname,id):
        cur.execute(f"delete from student where {columnname}={id}")
        conn.commit()