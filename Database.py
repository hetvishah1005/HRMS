import mysql.connector
import smtplib
from datetime import datetime, date
from tkinter import messagebox
import datetime
#from datetime import datetime
#from datetime import date
#import datetime
#import time


def loginCheck(uname, passwd):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * FROM login where username='"+uname+"' and password='"+passwd+"'")
#    con.execute("SELECT SELECT emp_id, emp_name, emp_gender, emp_dob, emp_age, emp_mobile, emp_address, emp_doj, emp_designation, emp_department FROM login emp_email=%s")
    rows = con.fetchone()
    #print(rows)
    return rows
    connect.close()

#============employee============
def insertEmp(ename, genedar, dob, age, mobile, hphone,  status, Addr, param, mail, doj, design, depart, educ, sal, photo, estatus):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("INSERT INTO employee (emp_name, emp_gender, emp_dob, emp_age, emp_mobile, emp_home_phone, emp_matiral_status, emp_address, emp_parmanent, emp_email, emp_doj, emp_designation, emp_department, emp_education, emp_basic_salary, emp_photo, emp_comp_status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (ename, genedar, dob, age, mobile, hphone, status, Addr, param, mail, doj, design, depart, educ, sal, photo, estatus))
    connect.commit()
    roll = "employee"
    con.execute("INSERT INTO login (name, username, password, roll) VALUES(%s, %s, %s, %s)", (ename, mail, mobile, roll))
    connect.commit()
    connect.close()

def fetch():
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * from Employee")
    rows = con.fetchall()
    #print(rows)
    return rows
    connect.close()


def remove(id, email):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    sql = "DELETE FROM employee WHERE emp_id= %s "
    adr = (id,)
    con.execute(sql, adr)
    print(con)
    connect.commit()
    con.execute("DELETE FROM login WHERE username= %s ", email)
    print(con)
    connect.commit()
    connect.close()

def updateEmp(id, ename, genedar, dob, age, mobile, hphone,  status, Addr, param, mail, doj, design, depart, educ, sal, estatus):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute(
            "UPDATE Employee SET emp_name=%s, emp_gender=%s, emp_dob=%s, emp_age=%s, emp_mobile=%s, emp_home_phone=%s, emp_matiral_status=%s, emp_address=%s, emp_parmanent=%s, emp_email=%s, emp_doj=%s, emp_designation=%s, emp_department=%s, emp_education=%s, emp_basic_salary=%s, emp_comp_status=%s where emp_id=%s",
            (ename, genedar, dob, age, mobile, hphone, status, Addr, param, mail, doj, design, depart, educ, sal, estatus, id))
    connect.commit()
    roll = "employee"
    #sql = f"UPDATE login SET username={mail}, password={mobile}, roll={roll} where name={ename}"
    #print(sql)
    con.execute("UPDATE login SET username=%s, password=%s, roll=%s where name=%s", (mail, mobile, roll, ename))
    print(con)
    connect.commit()
    connect.close()

#_______Department__________
def allDepartment():
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * from department")
    rows = con.fetchall()
    return rows
    connect.close()


def insertDepartment(dep_name, dep_head):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("INSERT INTO department (dep_name, dep_head) VALUES(%s, %s)", (dep_name, dep_head))
    connect.commit()
    connect.close()

def removeDemartment(id):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    sql = "DELETE FROM department WHERE dep_id= %s "
    adr = (id, )
    con.execute(sql, adr)
    print(con)
    connect.commit()
    connect.close()

def updateDepartment(id, dep_name, dep_head):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("UPDATE department SET dep_name=%s, dep_head=%s WHERE dep_id=%s", (dep_name, dep_head, id))
    connect.commit()
    connect.close()

#_______Award__________

def allAward():
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * from award")
    rows = con.fetchall()
    return rows
    connect.close()


def insertAward(dep_name, emp_name, aw_name, month, year):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("INSERT INTO award (dep_name, emp_name, aw_name, aw_month, aw_year) VALUES(%s, %s, %s, %s, %s)", (dep_name, emp_name, aw_name, month, year))
    connect.commit()
    connect.close()


def removeAward(id):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    sql = "DELETE FROM award WHERE aw_id= %s "
    adr = (id, )
    con.execute(sql, adr)
    #print(con)
    connect.commit()
    connect.close()


def updateAward(id, dep_name, emp_name, aw_name, month, year):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("UPDATE award SET dep_name=%s, emp_name=%s, aw_name=%s, aw_month=%s, aw_year=%s WHERE aw_id=%s", (dep_name, emp_name, aw_name, month, year, id))
    connect.commit()
    connect.close()


def getAll():
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * FROM employee")
    rows = con.fetchall()
    return rows
    connect.close()


def getPayroll(id):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    sql1 = "SELECT emp_id, emp_name, emp_gender, emp_dob, emp_doj, emp_mobile, emp_address, emp_email, emp_designation, emp_department, emp_basic_salary FROM employee WHERE emp_id=%s"
    adr = (id, )
    con.execute(sql1, adr)
    row = con.fetchone()
    return row
    connect.close()


def insertSalary(empId, empName, empDob, empDender, empDesignation, empDepartment, empMobile, empEmail, empAddress, empDoj, empBasicSalary, salMonth, salYear, totalDays, totalLeaves, esic, pf, convance, netPay):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("INSERT INTO salary (emp_id, emp_name, emp_dob, emp_gender, emp_designation, emp_department, emp_mobile, emp_email, emp_address, emp_doj, emp_basic_salary, sal_month, sal_year, total_days, total_leaves, esic, pf, convance, net_pay) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)", (empId, empName, empDob, empDender, empDesignation, empDepartment, empMobile, empEmail, empAddress, empDoj, empBasicSalary, salMonth, salYear, totalDays, totalLeaves, esic, pf, convance, netPay))
    connect.commit()
    connect.close()

#_______Department__________
def allLeave():
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * from empleave")
    rows = con.fetchall()
    #print(rows)
    return rows
    connect.close()

def insertLeave(eid, name, mob, mail, droplist_4, droplist_5, droplist_6, date0, morn, after, date1, date2, date3, droplist_12, reason):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("INSERT INTO empleave (emp_id, emp_name, emp_mobile, emp_email, emp_designation, emp_department, leave_type, leave_half_date, leave_morning, leave_noon, leave_full_date, leave_start_date, leave_end_date, leave_request, leave_reason) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" , (eid, name, mob, mail, droplist_4, droplist_5, droplist_6, date0, morn, after, date1, date2, date3, droplist_12, reason))
    connect.commit()
    connect.close()

def removeLeave(id):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    sql = "DELETE FROM empleave WHERE leave_id= %s "
    adr = (id, )
    con.execute(sql, adr)
    #print(con)
    connect.commit()
    connect.close()

def updateLeave(id, eid, name, mob, mail, droplist_4, droplist_5, droplist_6, date0, morn, after, date1, date2, date3, droplist_12, reason):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("UPDATE empleave SET emp_id=%s, emp_name=%s, emp_mobile=%s, emp_email=%s, emp_designation=%s, emp_department=%s, leave_type=%s, leave_half_date=%s, leave_morning=%s, leave_noon=%s, leave_full_date=%s, leave_start_date=%s, leave_end_date=%s, leave_request=%s, leave_reason=%s WHERE leave_id=%s", (eid, name, mob, mail, droplist_4, droplist_5, droplist_6, date0, morn, after, date1, date2, date3, droplist_12, reason, id))
    connect.commit()
    sender_email = "jeelpatel6294@gmail.com"
    sender_password = "9925692634"

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(sender_email, sender_password)
    print("LOGIN SUCCESSFULLY")
    address_info = mail
    email_info = f'''Dear {name},
                This is to inform that your Leave has been {droplist_12} by the HR.
                because your reason for {reason} is not valid or your leaves are more than 2.
                '''
    server.sendmail(sender_email, address_info, email_info)
    messagebox.showinfo("Success", "Email Send to the Employee")
    connect.close()


def insertAttendance(e_id, e_name, tdate, intime):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    print(e_id, e_name, tdate, intime)
    con.execute("INSERT INTO attendance (emp_id, emp_name, att_date, att_intime) VALUES(%s, %s, %s, %s)", (e_id, e_name, tdate, intime))
    connect.commit()
    connect.close()

def updateAttendance(e_id):
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * FROM attendance where emp_id='" + str(e_id) + "' ORDER BY att_id DESC LIMIT 1")
    #con.execute("SELECT * FROM attendance where emp_id='" + str(e_id) + "'")
    #print(con)
    rows = con.fetchone()
    print("updateAttendance")
    print(rows)
    now = datetime.now()
    outtime = now.strftime("%H:%M")
    print(outtime)
    con.execute("UPDATE attendance SET emp_id=%s, emp_name=%s, att_date=%s, att_intime=%s, att_outtime=%s where att_id=%s",(rows[1],rows[2],rows[3],rows[4],outtime,rows[0]))
    connect.commit()
    connect.close()

#fetch all
def fetch_all(uname):
    print(uname)
    todayDate = datetime.date.today()
    enddate = todayDate.strftime("%d/%m/%Y")
    if todayDate.day > 25:
        todayDate += datetime.timedelta(7)
    td = todayDate.replace(day=1)
    firstdate = td.strftime("%d/%m/%Y")
    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * FROM attendance WHERE att_date <= '"+enddate+"' and att_date >='"+firstdate+"'")
    rows = con.fetchone()
    return rows
    connect.close()
