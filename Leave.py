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
    #leave_typ = StringVar()
    date0 = StringVar()
    date1 = StringVar()
    date2 = StringVar()
    date3 = StringVar()
    #hdate = StringVar()
    #fdate = StringVar()
    #sdate = StringVar()
    #edate = StringVar()
    morn = StringVar()
    after = StringVar()
    reason = StringVar()

    def getLeave(event):
        selected_row = tv_leave.focus()
        data = tv_leave.item(selected_row)
        global row
        row = data["values"]
        #print(row)
        eid.set(row[0])
        name.set(row[2])
        mob.set(row[3])
        mail.set(row[4])
        droplist_4.set(row[5])
        droplist_5.set(row[6])
        droplist_6.set(row[7])
        date0.set(row[8])
        morn.set(row[9])
        after.set(row[10])
        date1.set(row[11])
        date2.set(row[12])
        date3.set(row[13])
        droplist_12.set(row[14])
        reason.set(row[15])

    def displayAllLeave():
        tv_leave.delete(*tv_leave.get_children())
        for rows in DB.allLeave():
            tv_leave.insert('', END, values=rows)


    def add_Leave():
        if eid.get()=="" or name.get()=="" or mob.get()=="" or mail.get()=="" or droplist_4.get()=="" or droplist_5.get()=="" or droplist_6.get()=="" or droplist_12.get()=="" or reason.get()=="":
            messagebox.showerror("Error in Input", "please fill  the details ")
            return
        # if eid.get() == "" or name.get() == "" or mob.get() == "" or mail.get() == "" or droplist_4.get() == "" or droplist_5.get() == "" or droplist_6.get() == "":
        #     messagebox.showerror("Error in Input", "please fill  the details ")
        #     return
        DB.insertLeave(eid.get(), name.get(), mob.get(), mail.get(), droplist_4.get(), droplist_5.get(), droplist_6.get(), date0.get(), morn.get(), after.get(), date1.get(), date2.get(), date3.get(), droplist_12.get(), reason.get())
        messagebox.showinfo("Success", "Record Inserted")
        clearall()
        displayAllLeave()

    def update_Leave():
        if eid.get()=="" or name.get()=="" or mob.get()=="" or mail.get()=="" or droplist_4.get()=="" or droplist_5.get()=="" or droplist_6.get()=="" or droplist_12.get()=="" or reason.get()=="":
            messagebox.showerror("Error in Input", "please fill  the details ")
            return
        DB.updateLeave(row[0], eid.get(), name.get(), mob.get(), mail.get(), droplist_4.get(), droplist_5.get(), droplist_6.get(), date0.get(), morn.get(), after.get(), date1.get(), date2.get(), date3.get(), droplist_12.get(), reason.get())
        messagebox.showinfo("Success", "Record Update")
        clearall()
        displayAllLeave()

    def delete_Leave():
        DB.removeLeave(row[0])
        messagebox.showinfo("Success", "Record Deleted")
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

    label_12 = Label(show_leave, text="Leave Request : ", font=("bold", 10))
    label_12.grid(row=10, column=0, padx=10, pady=10, sticky='w')
    list_of_Leavetype = ["Accepted", "Rejected"]

    droplist_12 = StringVar()
    droplist12 = OptionMenu(show_leave, droplist_12, *list_of_Leavetype)
    droplist12.config(width=25)
    droplist_12.set('--Select--')
    droplist12.grid(row=10, column=1, padx=10, pady=10, sticky='w')

    label_13 = Label(show_leave, text="Reason :", font=("bold", 10))
    label_13.grid(row=10, column=2, pady=10, padx=10, sticky=W)
    entry_13 = Entry(show_leave, textvariable=reason, width=30)
    entry_13.grid(row=10, column=3, pady=10, padx=10, sticky=W)

    #Button(root, text='Submit', width=20, bg="black", fg='white').grid(row=12, column=1, padx=10, pady=10, sticky='w')
    #Button(root, text='Reset', width=20, bg="black", fg='white').grid(row=12, column=2, padx=10, pady=10, sticky='w')

    btn_frame = Frame(show_leave)
    btn_frame.grid(row=11, column=0, columnspan=4, padx=10, pady=10, sticky="w")
    btnAdd = Button(btn_frame, command=add_Leave, text="Add Details", width=15, font=("Calibri", 16, "bold"),
                    fg="white", bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_Leave, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                     fg="white", bg="#2980b9", bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_Leave, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                       fg="white", bg="#c0392b", bd=0).grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearall, text="Clear Details", width=15, font=("Calibri", 16, "bold"),
                      fg="white", bg="#f39c12", bd=0).grid(row=0, column=3, padx=10)

    # Treeview Scrollbar
    # tree_scroll = Scrollbar(new_leave)
    # tree_scroll.pack(side=RIGHT, fill='y')
    tree_frame = Frame(new_leave, bg="#ecf0f1")
    tree_frame.place(x=0, y=450, width=1360, height=300)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tree_scroll1 = Scrollbar(tree_frame, orient='horizontal')
    tree_scroll1.pack(side=BOTTOM, fill=X)

    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 16),
                    rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))  # Modify the font of the headings
    tv_leave = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll1.set, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), style="mystyle.Treeview")

    tree_scroll.config(command=tv_leave.yview)
    tree_scroll1.config(command=tv_leave.xview)

    tv_leave.heading("1", text="Id")
    tv_leave.column("1", width=50, minwidth=150, anchor=CENTER)
    tv_leave.heading("2", text="Emp Id")
    tv_leave.column("2", width=100, minwidth=150, anchor=CENTER)
    tv_leave.heading("3", text="Employee Name ")
    tv_leave.column("3", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("4", text="Contact")
    tv_leave.column("4", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("5", text="Email")
    tv_leave.column("5",width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("6", text="Designation")
    tv_leave.column("6", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("7", text="Department Name")
    tv_leave.column("7", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("8", text="Leave Type")
    tv_leave.column("8", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("9", text="Half day Date")
    tv_leave.column("9", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("10", text="Morning")
    tv_leave.column("10", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("11", text="Afternoon")
    tv_leave.column("11", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("12", text="Full Day Date")
    tv_leave.column("12", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("13", text="Start Date")
    tv_leave.column("13", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("14", text="End Date")
    tv_leave.column("14", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("15", text="Leave Request")
    tv_leave.column("15", width=150, minwidth=250, anchor=CENTER)
    tv_leave.heading("16", text="Leave Reason")
    tv_leave.column("16", width=150, minwidth=250, anchor=CENTER)
    tv_leave['show'] = 'headings'
    tv_leave.bind("<ButtonRelease-1>", getLeave)
    tv_leave.pack(fill=X, expand="True")

    displayAllLeave()
    show_leave.mainloop()
