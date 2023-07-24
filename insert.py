import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Saicharan88@'
)

cur = conn.cursor()

class inserted:

    def departmentinsert(x,departmentid,departmentname):
        cur.execute(f"insert into department values({departmentid},'{departmentname}')")
        conn.commit()

    def courseinsert(x,courseid,coursename,coursefee,duration):
        cur.execute(f"insert into course values({courseid},'{coursename}',{coursefee},{duration})")
        conn.commit()

    def facultyinsert(x,facultyid,facultyname,departmentid,salary,courseid):
        cur.execute(f"insert into faculty values({facultyid},'{facultyname}',{departmentid},{salary},{courseid})")
        conn.commit()

    def studentinsert(x,sid,sname,courseid,departmentid):
        cur.execute(f"insert into student values({sid},'{sname}',{courseid},{departmentid})")
        conn.commit()

