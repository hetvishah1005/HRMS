from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import Database as DB

def leave_request(root):

    new_leave = Toplevel(root)
    new_leave.geometry("1920x1080+0+0")
    new_leave.title('Leave Application')
    new_leave.resizable(False, False)
    new_leave.config()
    new_leave.state("zoomed")

    eid = StringVar()
    name = StringVar()
    mob = StringVar()
    mail = StringVar()
    date0 = StringVar()
    date1 = StringVar()
    date2 = StringVar()
    date3 = StringVar()
    morn = StringVar()
    after = StringVar()
    reason = StringVar()

    def getLeave(event):
        pass

    def displayAllLeave():
        pass

    def add_Leave():
        if eid.get()=="" or name.get()=="" or mob.get()=="" or mail.get()=="" or droplist_4.get()=="" or droplist_5.get()=="" or droplist_6.get()=="" or droplist_12.get()=="" or reason.get()=="":
            messagebox.showerror("Error in Input", "please fill  the details ")
            return
        DB.insertLeave(eid.get(), name.get(), mob.get(), mail.get(), droplist_4.get(), droplist_5.get(), droplist_6.get(), date0.get(), morn.get(), after.get(), date1.get(), date2.get(), date3.get(), droplist_12.get(), reason.get())
        messagebox.showinfo("Success", "Record Inserted")
        clearall()
        displayAllLeave()

    def clearall():
        eid.set("")
        name.set("")
        mob.set("")
        mail.set("")
        droplist_4.set("--Select--")
        droplist_5.set("--Select--")
        droplist_6.set("--Select--")
        date0.set("")
        morn.set("")
        after.set("")
        date1.set("")
        date2.set("")
        date3.set("")
        droplist_12.set("--Select--")
        reason.set("")

    show_leave = Frame(new_leave)
    show_leave.pack(side=TOP, fill="both", anchor=CENTER)

    label_1 = Label(show_leave, text="Emp_ID :", font=("bold", 10))
    label_1.grid(row=2, column=0, pady=10, padx=10, sticky='w')
    entry_1 = Entry(show_leave, textvariable=eid, width=30)
    entry_1.grid(row=2, column=1, pady=10, padx=10, sticky='w')

    label_1 = Label(show_leave, text="Name :", font=("bold", 10))
    label_1.grid(row=2, column=2, pady=10, padx=10, sticky='w')
    entry_1 = Entry(show_leave, textvariable=name, width=30)
    entry_1.grid(row=2, column=3, pady=10, padx=10, sticky='w')

    label_2 = Label(show_leave, text="Contact No. :", font=("bold", 10))
    label_2.grid(row=2, column=4, sticky='w', pady=10, padx=10)
    entry_2 = Entry(show_leave, textvariable=mob, width=30)
    entry_2.grid(row=2, column=5, sticky='w', pady=10, padx=10)

    label_3 = Label(show_leave, text="Email ID :", font=("bold", 10))
    label_3.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    entry_3 = Entry(show_leave, textvariable=mail, width=30)
    entry_3.grid(row=3, column=1, padx=10, pady=10, sticky='w')

    label_4 = Label(show_leave, text="Designation :", font=("bold", 10))
    label_4.grid(row=3, column=2, padx=10, pady=10, sticky='w')

    list_of_designation = ["CHAIRMAN", "MD", "VICE PRESIDENT", "GENERAL MANAGER", "PROJECT HEAD", "PROJECT MANAGER",
                           "SALES EXECUTIVE", "PROJECT CO-ORDINATOR", "BACK OFFICE EXECUTIVE", "RECEPTIONIST",
                           "JUNIOR ACCOUNTANT", "SENIOR ACCOUNTANT", "ACCOUNT ASSISTANT", "ACCOUNT MANAGER",
                           "TENDER MANAGER", "TRAINER", "INTERN"]

    droplist_4 = StringVar()
    droplist4 = OptionMenu(show_leave, droplist_4, *list_of_designation)
    droplist4.config(width=25)
    droplist_4.set('--Select--')
    droplist4.grid(row=3, column=3, padx=10, pady=10, sticky='w')

    label_5 = Label(show_leave, text="Department :", font=("bold", 10))
    label_5.grid(row=3, column=4, padx=10, pady=10, sticky='w')

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT dep_name FROM department")
    my_data = con.fetchall()
    my_list = [r for r, in my_data]  # create a  list
    droplist_5 = StringVar(show_leave)
    droplist_5.set(my_list[0])  # default value
    droplist5 = OptionMenu(show_leave, droplist_5, *my_list)
    droplist5.grid(row=3, column=5, padx=10, pady=10, sticky='w')
    droplist5.config(width=25)
    droplist_5.set('--Select--')
    connect.close()

    label_6 = Label(show_leave, text="Leave Type :", font=("bold", 10))
    label_6.grid(row=6, column=0, padx=10, pady=10, sticky='w')

    list_of_Leavetype = ["HALF DAY", "FULL DAY", "MORE THEN ONE DAY"]

    droplist_6 = StringVar()
    droplist6 = OptionMenu(show_leave, droplist_6, *list_of_Leavetype)
    droplist6.config(width=25)
    droplist_6.set('--Select--')
    droplist6.grid(row=6, column=1, padx=10, pady=10, sticky='w')

    # First Row
    Label(show_leave, text='Half Day : ').grid(row=7, column=0, padx=10, pady=10, sticky='w')
    Label(show_leave, text='Date : ').grid(row=7, column=1, padx=10, pady=10, sticky='w')
    hdate = Entry(show_leave, textvariable=date0).grid(row=7, column=2, padx=10, pady=10, sticky='w')
    Label(show_leave, text='Morning :   ').grid(row=7, column=3, padx=10, pady=10, sticky='w')
    mor = Entry(show_leave, textvariable=morn).grid(row=7, column=4, padx=10, pady=10, sticky='w')
    Label(show_leave, text='Afternoon :  ').grid(row=7, column=5, padx=10, pady=10, sticky='w')
    aft = Entry(show_leave, textvariable=after).grid(row=7, column=6, padx=10, pady=10, sticky='w')

    # Second Row
    Label(show_leave, text='Full Day : ').grid(row=8, column=0, padx=10, pady=10, sticky='w')
    Label(show_leave, text='Date : ').grid(row=8, column=1, padx=10, pady=10, sticky='w')
    fdate = Entry(show_leave, textvariable=date1).grid(row=8, column=2, padx=10, pady=10, sticky='w')

    # Third Row
    Label(show_leave, text='More Than One Day : ').grid(row=9, column=0, padx=10, pady=10, sticky='w')
    Label(show_leave, text='Start Date :').grid(row=9, column=1, padx=10, pady=10, sticky='w')
    sdate = Entry(show_leave, textvariable=date2).grid(row=9, column=2, padx=10, pady=10, sticky='w')
    Label(show_leave, text='End Date :').grid(row=9, column=3, padx=10, pady=10, sticky='w')
    edate = Entry(show_leave, textvariable=date3).grid(row=9, column=4, padx=10, pady=10, sticky='w')

    label_13 = Label(show_leave, text="Reason :", font=("bold", 10))
    label_13.grid(row=9, column=5, pady=10, padx=10, sticky=W)
    entry_13 = Entry(show_leave, textvariable=reason, width=30)
    entry_13.grid(row=9, column=6, pady=10, padx=10, sticky=W)


    btn_frame = Frame(show_leave)
    btn_frame.grid(row=11, column=0, columnspan=4, padx=10, pady=10, sticky="w")
    btnAdd = Button(btn_frame, command=add_Leave, text="Add Details", width=15, font=("Calibri", 16, "bold"),
                    fg="white", bg="#16a085", bd=0).grid(row=0, column=0)
    btnClear = Button(btn_frame, command=clearall, text="Clear Details", width=15, font=("Calibri", 16, "bold"),
                      fg="white", bg="#f39c12", bd=0).grid(row=0, column=3, padx=10)

    label_12 = Label(show_leave, text="Leave Request : ", font=("bold", 10), state="disabled")
    label_12.grid(row=10, column=0, padx=10, pady=10, sticky='w')
    list_of_Leavetype = ["Accepted", "Rejected"]

    droplist_12 = StringVar()
    droplist12 = OptionMenu(show_leave, droplist_12, *list_of_Leavetype)
    droplist12.configure(state="disabled")
    droplist12.config(width=25)
    droplist_12.set('--Select--')
    droplist12.grid(row=10, column=1, padx=10, pady=10, sticky='w')



    show_leave.mainloop()
