import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="management"
)

cursor = con.cursor()


def insertemployee(arg):
    print(arg)
    try:
        cursor.execute(
            "insert into employee_table (name,pno,address,email,designation,gender,password) values(%s,%s,%s,%s,%s,%s,%s)",
            arg)
        con.commit()
        return True
    except:
        return False


def loginuser(arg):
    try:
        cursor.execute("select * from login_page where Email=%s and Password=%s", arg)
        return cursor.fetchone()
    except:
        return False


def showemployee():
    cursor.execute("select * from employee_table")
    return cursor.fetchall()


def deleteemployee(arg):
    cursor.execute("delete from employee_table where id=%s", arg)
    con.commit()
    return True


def updateemployee(arg):
    print("Database update employee - ", arg)
    try:
        cursor.execute(
            "update employee_table set name=%s,pno=%s,address=%s,email=%s,designation=%s,gender=%s where id=%s", arg)
        con.commit()
        return True
    except:
        return False


def showpendingtask(*arg):
    cursor.execute("select * from task_table where emp_email=%s and status=%s", arg)
    return cursor.fetchall()


def showcompletedtask(*arg):
    cursor.execute("select * from task_table where emp_email=%s and status=%s", arg)
    return cursor.fetchall()


def deletetask(arg):
    cursor.execute("delete from task_table where id=%s", arg)
    con.commit()
    return True


def update_task(arg):
    print("Data in task_management - ", arg)
    cursor.execute("update task_table set task_name=%s,description=%s where id=%s",
                   arg)
    con.commit()
    return True


def update_assign_task(*arg):
    print("Data in task_management - ", arg)
    cursor.execute("update task_table set start_date=%s,end_date=%s,status=%s,emp_email=%s where task_name=%s",
                   arg)
    con.commit()
    return True


def inserttask(*arg):
    print("Data Received in database - ", arg)

    try:
        cursor.execute(
            "insert into task_table(task_name,description) values(%s,%s)",
            arg)

        con.commit()
        return True
    except:
        return False


def showtasks():
    cursor.execute("select * from task_table")
    return cursor.fetchall()

def assign_task(*arg):
    print("Assign Task Data - ", arg)
    try:
        cursor.execute("update task_table set status=%s, emp_email=%s, start_date=%s, end_date=%s where id=%s", arg)
        con.commit()
        return True
    except:
        return False