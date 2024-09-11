import tkinter
import shutil
from tkinter import *
from tkinter import ttk
from datetime import datetime, date
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
import Attendance
import login
import leaveE
import profile
import Holiday
import Database as DB


#method to call login
def loginemp(root):
    login.logingtosystem(root)

    # Method to call Attendance
def showattendance(root,uname):
    Attendance.show_attend(root,uname)

#Method to call profile
def NewProfile(root, uname):
   profile.my_profile(root, uname[1])

#Method to call Leave
def showLeaveRequest(root):
    leaveE.leave_request(root)

#Method to call Holiday
def addHoliday(root):
    Holiday.add_Holiday(root)
def listHoliday(root):
    Holiday.listofHoliday(root)


def setAttendance(eid, e_name):
    today = date.today()
    tday = str(today.strftime("%d/%m/%Y"))
    now = datetime.now()
    intime = now.strftime("%H:%M")
    #outtime = '00:00'
    DB.insertAttendance(eid, e_name, tday, intime)
    messagebox.showinfo("Attendance", "You are logged in")


def updateAttendance(eid):
    DB.updateAttendance(eid)
    messagebox.showinfo("Attendance", "you are logged out")


def main(uname):
    root = Toplevel()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.resizable(False, False)
    root.config()
    root.state("zoomed")
    print(uname)

    title = Label(root, text='Gujarat Infotech Limited', bg='light green', fg='white', font=('calibri', 25, 'bold'),
                  relief=GROOVE, anchor=tkinter.CENTER, bd=5)
    title.pack(fill=X, ipady=2)
    welcome = Label(title, text=f"welcome:\n"
                                f"{uname}", bg='light green', font=('calibri', 15, 'bold'), padx=10)
    welcome.pack(side=RIGHT, pady=10)
    image = Image.open(r"image/GIL.png")
    img_resize = image.resize((100, 80))
    img = ImageTk.PhotoImage(img_resize)
    logo = Button(title, image=img, bg='grey')
    logo.image = img
    logo.pack(side=LEFT, padx=20, pady=0)

    # ====================let frame========================

    f1 = Frame(root, bg='violet', relief=RIDGE, bd=3)
    f1.place(x=0, y=100, width=200, height=680)

    # ====================Attendance========================
    attnd = Menubutton(f1, text='Attendance', relief=tkinter.SUNKEN, bg='purple', fg='white', padx=20, pady=6,
                       font=("Calibri", 18))
    attnd.menu = Menu(attnd, tearoff=0)
    attnd["menu"] = attnd.menu

    attnd.menu.add_command(label='Show Attendance', command=lambda: showattendance(root,uname), font=("Calibri", 12))
    attnd.pack(pady=15)

    # ====================Leave========================

    leave = Menubutton(f1, text='Leave', relief=tkinter.SUNKEN,bg='purple',fg='white', padx=48, pady=6, font=("Calibri", 18))
    leave.menu = Menu(leave, tearoff=0)
    leave["menu"] = leave.menu

    leave.menu.add_command(label='Apply For Leave', command=lambda: showLeaveRequest(root), font=("Calibri", 12))
    leave.pack(pady=20)
    # ====================Holiday========================

    holiday = Menubutton(f1, text='Holiday', bg='purple', fg='white', relief=tkinter.SUNKEN, padx=40, pady=6, font=("Calibri", 18))
    holiday.menu = Menu(holiday, tearoff=0)
    holiday["menu"] = holiday.menu

    holiday.menu.add_command(label="List Of Holiday", command=lambda: listHoliday(root), font=("Calibri", 12))
    holiday.pack(pady=20)

       #rigth frame
    r1 = Frame(root, relief=RIDGE, bd=8, bg="deeppink3")
    r1.place(x=200, y=100, width=1165, height=615)

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    sql = "SELECT * from employee where emp_name=%s"
    adr = (uname,)
    con.execute(sql, adr)
    # print(sql)
    # con.execute(sql)
    row = con.fetchone()
    print(row)
    left_lbl = Label(r1, bg="steelblue", bd=0)
    left_lbl.place(x=0, y=0, relheight=1, width=570)

    right_lbl = Label(r1, bg="brown", bd=0)
    right_lbl.place(x=570, y=0, relwidth=0.504, relheight=1)

    label = Label(r1, relief=RIDGE, bd=0)
    label.place(x=130, y=30, height=550, width=875)

    title = Label(label, text="PROFILE", font=("calibri", 30, "bold"), bg="lightblue", fg="white", padx=10,
                  relief=GROOVE, anchor=CENTER, bd=5).place(x=0, y=0, relwidth=1)

    image = Image.open(r"image/pro.png")
    img_resize = image.resize((110, 130))
    img = ImageTk.PhotoImage(img_resize)
    logo = Label(label, image=img)
    logo.image = img
    logo.pack(side=LEFT, padx=150, pady=80, anchor="nw")

    # Create Attendance in and out time
    intym = Button(label, text="I AM IN", command=lambda: setAttendance(row[0], row[1]), font=("calibri", 15, "bold"),
                   fg="Black", relief=GROOVE, bg="lightgreen", bd=2, width=12)
    intym.pack(side=LEFT, padx=50, pady=100, anchor="nw")

    outtym = Button(label, text="I AM OUT", command=lambda: updateAttendance(row[0]),
                    font=("calibri", 15, "bold"),
                    fg="Black", relief=GROOVE, bg="Red", bd=2, width=12)
    outtym.pack(side=LEFT, padx=5, pady=100, anchor='ne')

    name = Label(label, text="Name :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=250)
    txt_name = Label(label, text=f"{row[1]}", font=("calibri", 15)).place(x=190, y=250)

    e_id = Label(label, text="Employee Id :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=250)
    txt_eid = Label(label, text=f"{row[0]}", font=("calibri", 15)).place(x=680, y=250)

    email = Label(label, text="Age :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=300)
    txt_email = Label(label, text=f"{row[4]}", font=("calibri", 15)).place(x=190, y=300)

    phoneno = Label(label, text="Phone No :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=300)
    txt_phoneno = Label(label, text=f"{row[5]}", font=("calibri", 15)).place(x=680, y=300)

    dob = Label(label, text="Birth Date :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=350)
    txt_dob = Label(label, text=f"{row[3]}", font=("calibri", 15)).place(x=190, y=350)

    gender = Label(label, text="Gender :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=350)
    txt_gender = Label(label, text=f"{row[2]}", font=("calibri", 15), bd=2).place(x=680, y=350)

    Address = Label(label, text="Address :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=400)
    txt_address = Label(label, text=f"{row[8]}", font=("calibri", 15)).place(x=190, y=400)

    doj = Label(label, text="Joining Date :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=400)
    txt_doj = Label(label, text=f"{row[11]}", font=("calibri", 15)).place(x=680, y=400)

    dep = Label(label, text="Department :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=450)
    txt_dep = Label(label, text=f"{row[13]}", font=("calibri", 15)).place(x=190, y=450)

    des = Label(label, text="Designation :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=450)
    txt_des = Label(label, text=f"{row[12]}", font=("calibri", 15)).place(x=680, y=450)
    connect.close()
    # =====================  bottom  ===========================

    footer = Label(root, text='COPYRIGHT(c) 2009 GUJARATINFOTECH.COM. ALL RIGHTS RESERVED.', bg='orange', fg='white',
                   font=('calibri', 15, 'bold'), relief=tkinter.SUNKEN, bd=2, anchor=tkinter.S)
    footer.pack(side=tkinter.BOTTOM, fill=X)
