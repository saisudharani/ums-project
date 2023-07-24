import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Saicharan88@'
)

cur = conn.cursor()

class updated:
    
    def deptupdate(x,colname,newval,oldval):
        cur.execute(f"update department set {colname}='{newval}' where {colname}='{oldval}'")
        conn.commit()

    def crupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update course set {columnname}='{newvalue}' where {columnname}='{oldvalue}'")
        conn.commit()
        
    def fcupdate(x,colname,newval,oldval):
        cur.execute(f"update faculty set {colname}='{newval}' where {colname}='{oldval}'")
        conn.commit()
    
    def stupdate(x,column,newcol,oldcal):
        cur.execute(f"update student set {column}='{newcol} where {column}='{oldcal}'")
        conn.commit()

obj=updated()

obj.deptupdate('departmentname','java','python')

     