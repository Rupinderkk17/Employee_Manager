import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="management"
)
cursor = con.cursor()

def loginuser(arg):
    print("Login Credentials ", arg)
    try:
        cursor.execute("select * from employee_table where email=%s and password=%s", arg)
        return cursor.fetchone()
    except:
        return False


def showpendingtask(*arg):
    print('argument are ', arg)
    try:
        cursor.execute("select * from task_table where emp_email=%s and status=%s", arg)
        return cursor.fetchall()
    except:
        return


def showcompletetask(*arg):
    try:
        cursor.execute("select * from task_table where emp_email=%s and status=%s", arg)
        return cursor.fetchall()
    except:
        return