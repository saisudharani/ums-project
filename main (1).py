from insert import inserted
from update import updated
from delete import deleted
from read import read

obj=inserted()
obj1=updated()
obj2=deleted()
obj3=read()
# obj.departmentinsert(20,'python')

print("Welcome to the University Management System!")
print("Database Information:")
print("- Number of tables: 4")
print("- Table names: Student, Department, Faculty, Course")

# Displaying student table information
print("\nStudent Table Information:")
print("- Number of records: 4")
print("- Columns: sid, sname, courseid, dptid")

# Displaying department table information
print("\nDepartment Table Information:")
print("- Number of records: 2")
print("- Columns: departmentid, departmentname")

# Displaying faculty table information
print("\nFaculty Table Information:")
print("- Number of records: 5")
print("- Columns: facultyid, facultyname, departmentid, salary, courseid")

# Displaying course table information
print("\nCourse Table Information:")
print("- Number of records: 4")
print("- Columns: courseid, coursename, coursefees, duration")

print('---------------------------------------------------------------------')

# print('for inserting the data in departmnet table press - 1')

# tab=int(input("please enter the number to insert data in table"))

'''if tab==1:
    dtid=int(input("please enter dptid"))
    dtname=input("please enter department name")
    obj.departmentinsert(dtid,dtname)'''

print('** you can do 4 operations on database **')
print('for adding the data write *add*')
print('for update the data write *update*')
print('for delete the data write *delete*')
print('for read the data write *read*')

opr = input('enter any operation')

if opr=='add':
    print('for inserting the data in departmnet table press - 1')
    print('for inserting the data in course table please press - 2: ')
    print('for inserting the data in faculty table please press - 3: ')


    tab=int(input("please enter the number to insert data in table"))

    if tab==1:
        dtid=int(input("please enter dptid"))
        dtname=input("please enter department name")
        obj.departmentinsert(dtid,dtname)

    if tab==2:
        crid=int(input("please enter courseid"))
        crname=input("please enter course name")
        crfee=int(input("please enter coursefee"))
        dura=int(input("please enter duration"))
        obj.courseinsert(crid,crname,crfee,dura)

    if tab==3:
        fcid=int(input("please enter facultyID: "))
        fcname=input("please enter faculty name: ")
        depid=int(input("please enter depart id: "))
        sal=int(input("please enter salary: "))
        crid=int(input("please enter course id: "))
        obj.facultyinsert(fcid,fcname,depid,sal,crid)
    

if opr=='update':

    print('for updating the data in department table please press - 1')
    print('for updating data in course table please press - 2: ')
    print('for updating data in faculty table please press - 3:')
    print('for updating the data in student table please press - 4: ')

    tab=int(input("please enter the number to update data in table"))

    if tab==1:
        col=input("please enter the column name: ")
        new=input("please enter the new value: ")
        old=input("please enter the old value: ")
        obj1.deptupdate(col,new,old)
    
    if tab==2:
        column=input("please enter the columnn name: ")
        new=input("please enter new column name: ")
        old=input("please enter old value: ")
        obj1.crupdate(column,new,old)

    if tab==3:
        col=input("please enter the column name: ")
        new=input("please enter new value: ")
        old=input("please enter old value: ")
        obj1.fcupdate(col,new,old)

    if tab==4:
        col=input("please enter the column name: ")
        new=input("please enter new value: ")
        old=input("please enter old value: ")
        obj1.stupdate(col,new,old)
    


if opr=='delete':

    print('for delete data in department table please press - 1: ')
    print('for deleting data in course table please press - 2: ')
    print('for deleting data in faculty table please press - 3:')
    print('for deleting data in student table please press - 4:')

    tab=int(input('enter any number to delete data in table'))

    if tab==1:
        col=input("please enter the column name: ")
        id=int(input("please enter the departmentid to delete data: "))
        obj2.deptdelete(col,id)

    if tab==2:
        column=input("please enter column name: ")
        id=int(input("please enter the id"))
        obj2.crdelete(column,id)
    
    if tab==3:
        column=input("please enter column name: ")
        id=int(input("please enter the id"))
        obj2.fcdelete(column,id)

    if tab==4:
        column=input("please enter column name: ")
        id=int(input("please enter the id"))
        obj2.stdelete(column,id)


if opr == "read":
    print('for read data in department table please press - 1: ')
    print('for read data in course table please press - 2: ')
    print('for read data in faculty table please press - 3:')
    print('for read data in student table please press - 4:')

    tab=int(input('enter any number to read data in table'))

    if tab==1:
        obj3.departmentread()

    if tab==2:
        obj3.courseread()

    if tab==3:
        obj3.facultyread()

    if tab==4:
        obj3.studentread()

    


