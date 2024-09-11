import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
#from tkinter import messagebox
from tkinter.filedialog import askopenfile
import mysql.connector
import io
from datetime import date
import login
import Employee
import Leave
import department
import Holiday
import award
import payroll
#import Database as DB

#method to call login
# def loginemp(root):
#     login.logingtosystem(root)

#Method to call Employee
def addNewEmp(root):
    Employee.add_emp(root)
def listEmp(root):
    Employee.listOfEmp(root)

#Method to call Employee
def addNewDep(root):
    department.add_department(root)

#Method to Payroll
def addPayroll(root):
    payroll.add_payroll(root)

#Method to calll Leave
def showLeaveRequest(root):
    Leave.leave_request(root)

#Method to call Holiday
def addHoliday(root):
    Holiday.add_Holiday(root)
def listHoliday(root):
    Holiday.listofHoliday(root)

#Method to call Award
def addNewAward(root):
    award.add_award(root)

#main ke under
#global flag variable banana hoga login on-off
#if flagvarname, login==off:
#open(login module)
#login.destroy login vali file

def main(row):
    root = Toplevel()
    root.title("Human Resource Management System")
    root.geometry("1920x1080+0+0")
    root.resizable(False, False)
    root.config()
    root.state("zoomed")

    # root = Tk()
    # root.title("Employee Management System")
    # root.geometry("1920x1080+0+0")
    # root.resizable(False, False)
    # root.config(bg="#2c3e50")
    # root.state("zoomed")
    #print(root)
    # global login
    # if login == OFF:
    #     open(login)

    # ===================heading==========================#

    title = Label(root, text='Gujarat Infotech Limited', bg='orange', fg='white', font=('calibri', 25, 'bold'),
                  relief=GROOVE, anchor=tkinter.CENTER, bd=5)
    title.pack(fill=X, ipady=2)
    welcome = Label(title, text='Welcome: \n'
                                f"{row[1]}", bg='orange', font=('calibri', 15, 'bold'), padx=10)
    welcome.pack(side=RIGHT, pady=10)
    image = Image.open(r"image/GIL.png")
    img_resize = image.resize((100, 80))
    img = ImageTk.PhotoImage(img_resize)
    logo = Label(title, image=img)
    logo.image = img
    logo.pack(side=LEFT, padx=20, pady=0)

    # ====================left frame========================


    f1 = Frame(root, bg='light blue', relief=RIDGE, bd=3)
    f1.place(x=0, y=100, width=180, height=700)

    # ====================Employee========================

    emp = Menubutton(f1, text='Employee',bg="deeppink4", fg="white", relief=tkinter.SUNKEN, padx=20, pady=6, font=("Calibri", 18))
    #emp.pack(pady=20, text="LEFT")
    emp.menu = Menu(emp, tearoff=0)
    emp["menu"] = emp.menu

    # emp.menu.add_command(label="List Of Employee")
    emp.menu.add_command(label="Add New Employee", command=lambda: addNewEmp(root), font=("Calibri", 12))
    emp.pack(pady=20, ipadx=10)

    # ====================Department========================

    depart = Menubutton(f1, text='Department',bg="deeppink4", fg="white", relief=tkinter.SUNKEN, padx=10, pady=6, font=("Calibri", 18))
    depart.menu = Menu(depart, tearoff=0)
    depart["menu"] = depart.menu

    depart.menu.add_command(label="List Of Department", command=lambda: addNewDep(root), font=("Calibri", 12))
    depart.pack(pady=20, ipadx=10)

    # ====================Payroll========================

    payroll = Menubutton(f1, text='Payroll', bg="deeppink4", fg="white", relief=tkinter.SUNKEN, padx=36, pady=6, font=("Calibri", 18))
    payroll.menu = Menu(payroll, tearoff=0)
    payroll["menu"] = payroll.menu

    payroll.menu.add_command(label="Calculate Payroll", command=lambda: addPayroll(root), font=("Calibri", 12))
    payroll.pack(pady=20, ipadx=10)

    # ====================Leave========================

    leave = Menubutton(f1, text='Leave',bg="deeppink4", fg="white", relief=tkinter.SUNKEN, padx=40, pady=6, font=("Calibri", 18))
    leave.menu = Menu(leave, tearoff=0)
    leave["menu"] = leave.menu

    leave.menu.add_command(label='Show Leave Request', command=lambda: showLeaveRequest(root), font=("Calibri", 12))
    leave.pack(pady=20, ipadx=10)

    # ====================Award========================

    award = Menubutton(f1, text='Awards',bg="deeppink4", fg="white", relief=tkinter.SUNKEN, padx=34, pady=6, font=("Calibri", 18))
    award.menu = Menu(award, tearoff=0)
    award["menu"] = award.menu

    award.menu.add_command(label="List Of Awards", command=lambda: addNewAward(root), font=("Calibri", 12))
    award.pack(pady=20, ipadx=10)

    # ====================Holiday========================

    holiday = Menubutton(f1, text='Holiday',bg="deeppink4", fg="white", relief=tkinter.SUNKEN, padx=42, pady=6, font=("Calibri", 18))
    holiday.menu = Menu(holiday, tearoff=0)
    holiday["menu"] = holiday.menu

    holiday.menu.add_command(label="List Of Holiday", command=lambda: listHoliday(root), font=("Calibri", 12))
    # holiday.menu.add_command(label="Add Holiday", command=lambda: addHoliday(root))
    holiday.pack(pady=20)

    # ====================right frame========================

    r1 = Frame(root, relief=RIDGE, bd=3)
    # r1.place(x=203, y=100, width=1156, height=580)
    r1.place(x=182, y=100, width=1320, height=700)

    btn_frame = Frame(r1, bg="#535c68")
    btn_frame.grid(row=1, column=0, padx=0, pady=0, sticky="w")
    btnEmp_month = Button(btn_frame, text="Emp of the Month", width=27, height=2, font=("Calibri", 16, "bold"),
                          fg="white", bg="#16a085",
                          bd=0).grid(row=0, column=0)
    btnleaveStatus = Button(btn_frame, text="Emp Leave Application Status ", width=25, height=2,
                            font=("Calibri", 16, "bold"), fg="white",
                            bg="#2980b9", bd=0).grid(row=0, column=1)
    btnAddSome = Button(btn_frame, text=" Emp Birthday", width=25, height=2, font=("Calibri", 16, "bold"), fg="white",
                        bg="#c0392b", bd=0).grid(row=0, column=2)
    btnAddSome1 = Button(btn_frame, text="Emp Anniversary", width=28, height=2, font=("Calibri", 16, "bold"),
                         fg="white",
                         bg="#f39c12", bd=0).grid(row=0, column=3)

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT dep_name, emp_name FROM award ORDER BY aw_id DESC LIMIT 1")
    data = con.fetchone()
    connect.close()
    lblEM = Label(btn_frame, text=f"{data}", width=27, font=("Calibri", 16, "bold"), fg="white",
                  bg="#16a085", bd=0).grid(row=1, column=0, pady=2)

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * FROM empleave WHERE MONTH(leave_full_date) = MONTH(CURRENT_DATE()) AND YEAR(leave_full_date) = YEAR(CURRENT_DATE())")
    cou = 0;
    for cou in con.fetchall():
        cou = cou + 1
    connect.close()
    lblleave = Label(btn_frame, text=f"{cou}", width=25, font=("Calibri", 16, "bold"), fg="white",
                     bg="#2980b9", bd=0).grid(row=1, column=1, ipadx=2, pady=2)
    today = date.today()
    d1 = str(today.strftime("%d/%m/%Y"))
    #print(d1)

    #declare @StartDate DATE
    #declare @EndDate DATE

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    #sql1 = "SELECT emp_name FROM employee WHERE DAY(emp_dob) = DAY(GETDATE())  AND MONTH([emp_dob]) = MONTH(GETDATE())"
    #sql1= "SELECT emp_name FROM employee WHERE DATEPART( Week, DATEADD( Year, DATEPART( Year, GETDATE()) - DATEPART( Year, emp_dob), emp_dob)) = DATEPART( Week, GETDATE());"
    sql1 = "SELECT emp_dob FROM employee WHERE emp_dob=%s"
    adr = (d1, )
    con.execute(sql1, adr)
    row = con.fetchone()
    connect.close()
    lblA1 = Label(btn_frame, text=f"{row}", width=25, font=("Calibri", 16, "bold"), fg="white",
                  bg="#c0392b", bd=0).grid(row=1, column=2, ipadx=2, pady=2)

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    sql2 = "SELECT emp_doj FROM employee WHERE emp_doj=%s"
    adr = (d1, )
    con.execute(sql2, adr)
    row1 = con.fetchone()
    connect.close()
    lblA2 = Label(btn_frame, text=f"{row1}", width=28, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",bd=0).grid(row=1, column=3,  pady=2)


    footer = Label(root, text='COPYRIGHT(c) 2009 GUJARATINFOTECH.COM. ALL RIGHTS RESERVED.', bg='orange', fg='white',
                   font=('calibri', 15, 'bold'), relief=tkinter.SUNKEN, bd=2, anchor=tkinter.S)
    footer.pack(side=tkinter.BOTTOM, fill=X)

    root.mainloop()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#       main()


