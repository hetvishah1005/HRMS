from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkcalendar import *
import time
import mysql.connector
import Database as DB

def add_emp(root):

    ename = StringVar()
    dob = StringVar()
    age = StringVar()
    mobile = StringVar()
    hphone = StringVar()
    mail = StringVar()
    doj = StringVar()
    sal = StringVar()

    # connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    # con = connect.cursor()
    # con.execute("SELECT dep_name FROM department")
    # my_data = con.fetchall()
    # my_list = [r for r, in my_data]  # create a  list

    new_emp = Toplevel(root)
    new_emp.geometry("1920x1080+0+0")
    new_emp.resizable(False, False)
    new_emp.config()
    new_emp.state("zoomed")
    new_emp.title('New Employee Registration form')

    # Entries Frame
    entries_frame = Frame(new_emp)
    entries_frame.pack(side=TOP, fill=X)

    title = Label(entries_frame, text="Add New Employee Details :", font=("Calibri", 18, "bold"))
    title.grid(row=0, columnspan=2, padx=10, pady=0, sticky="w")

    lbl_1 = Label(entries_frame, text="Full Name :", font=("Calibri", 12))
    lbl_1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_1 = Entry(entries_frame, textvariable=ename, font=("Calibri", 12), width=25)
    entry_1.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    lblGender = Label(entries_frame, text="Gender :", font=("Calibri", 12))
    lblGender.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    list_of_gender = ["Male", "Female", "Other"]
    droplist_g = StringVar()
    droplistg = OptionMenu(entries_frame, droplist_g, *list_of_gender)
    droplistg.grid(row=1, column=3, padx=10, pady=10, sticky="w")
    droplistg.config(width=25)
    droplist_g.set('--Select--')

    lbldob = Label(entries_frame, text="D.O.B :", font=("Calibri", 12))
    lbldob.grid(row=1, column=4, padx=10, pady=5, sticky="w")
    txtDob = DateEntry(entries_frame, width=25, textvariable=dob, background= "magenta3", foreground= "white", bd=2)
    txtDob.grid(row=1, column=5, padx=10, pady=5, sticky="w")

    lbl_age = Label(entries_frame, text="Age :", font=("Calibri", 12))
    lbl_age.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_age = Entry(entries_frame, textvariable=age, font=("Calibri", 12), width=25)
    entry_age.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    lblContact = Label(entries_frame, text="Mobile No. :", font=("Calibri", 12))
    lblContact.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    txtContact = Entry(entries_frame, textvariable=mobile, font=("Calibri", 12), width=25)
    txtContact.grid(row=2, column=3, padx=10, sticky="w")

    lblContact1 = Label(entries_frame, text="phone Home : :", font=("Calibri", 12))
    lblContact1.grid(row=2, column=4, padx=10, pady=5, sticky="w")
    txtContact1 = Entry(entries_frame, textvariable=hphone, font=("Calibri", 12), width=25)
    txtContact1.grid(row=2, column=5, padx=5, sticky="w")

    lblAddress = Label(entries_frame, text="Address :", font=("Calibri", 12))
    lblAddress.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    txtAddress = Text(entries_frame, width=25, height=3, font=("Calibri", 12))
    txtAddress.grid(row=3, column=1, columnspan=4, padx=10, sticky="w")

    lblAddress1 = Label(entries_frame, text="Permanent Addr. :", font=("Calibri", 12))
    lblAddress1.grid(row=3, column=2, padx=10, pady=5, sticky="w")
    txtAddress1 = Text(entries_frame, width=25, height=3, font=("Calibri", 12))
    txtAddress1.grid(row=3, column=3, columnspan=3, padx=10, sticky="w")

    lblstatus = Label(entries_frame, text="Marriage Status :", font=("Calibri", 12))
    lblstatus.grid(row=3, column=4, padx=10, pady=5, sticky="w")
    list_of_designation = ["Married", "Unmarried"]
    droplist_s = StringVar()
    droplists = OptionMenu(entries_frame, droplist_s, *list_of_designation)
    droplists.grid(row=3, column=5, padx=10, pady=10, sticky="w")
    droplists.config(width=25)
    droplist_s.set('--Select--')

    lblEmail = Label(entries_frame, text="Email :", font=("Calibri", 12))
    lblEmail.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    txtEmail = Entry(entries_frame, textvariable=mail, font=("Calibri", 12), width=25)
    txtEmail.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    lbldoj = Label(entries_frame, text="D.O.J", font=("Calibri", 12))
    lbldoj.grid(row=4, column=2, padx=10, pady=5, sticky="w")
    txtDoj = DateEntry(entries_frame, width=25, textvariable=doj, background="magenta3", foreground="white", bd=2)
    txtDoj.grid(row=4, column=3, padx=10, pady=5, sticky="w")

    lbldesign = Label(entries_frame, text="Designation :", font=("Calibri", 12))
    lbldesign.grid(row=4, column=4, padx=10, pady=5, sticky="w")
    list_of_designation = ["CHAIRMAN", "MD", "VICE PRESIDENT", "GENERAL MANAGER", "PROJECT HEAD", "PROJECT MANAGER",
                           "SALES EXECUTIVE", "PROJECT CO-ORDINATOR", "BACK OFFICE EXECUTIVE", "RECEPTIONIST",
                           "JUNIOR ACCOUNTANT", "SENIOR ACCOUNTANT", "ACCOUNT ASSISTANT", "ACCOUNT MANAGER",
                           "TENDER MANAGER", "TRAINER", "INTERN"]

    droplist_d = StringVar()
    droplistd = OptionMenu(entries_frame, droplist_d, *list_of_designation)
    droplistd.config(width=25)
    droplist_d.set('--Select--')
    droplistd.grid(row=4, column=5, padx=10, pady=5, sticky="w")

    label_5 = Label(entries_frame, text="Department :", font=("Calibri", 12))
    label_5.grid(row=5, column=0, padx=10, pady=5, sticky="w")

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT dep_name FROM department")
    my_data = con.fetchall()
    my_list = [r for r, in my_data]  # create a  list
    droplist_1 = StringVar(entries_frame)
    droplist_1.set(my_list[0])  # default value
    droplist1 = OptionMenu(entries_frame, droplist_1, *my_list)
    droplist1.grid(row=5, column=1, padx=10, pady=10, sticky="w")
    droplist1.config(width=25)
    droplist_1.set('--Select--')
    connect.close()

    lbledu = Label(entries_frame, text="Education :", font=("Calibri", 12))
    lbledu.grid(row=5, column=2, padx=10, pady=5, sticky="w")
    list_of_Education = ["BE/B.Tech", "Bsc", "Diploma in Computer", "Msc", "ME/M.Tech", "Phd"]
    droplist_2 = StringVar()
    droplist2 = OptionMenu(entries_frame, droplist_2, *list_of_Education)
    droplist2.grid(row=5, column=3, padx=15, pady=10, sticky="w")
    droplist2.config(width=25)
    droplist_2.set('--Select--')

    lblsal = Label(entries_frame, text="Basic Salary", font=("Calibri", 12))
    lblsal.grid(row=5, column=4, padx=10, pady=5, sticky="w")
    txtsal = Entry(entries_frame, textvariable=sal, font=("Calibri", 12), width=25)
    txtsal.grid(row=5, column=5, padx=10, pady=5, sticky="w")

    global filename   # For access both function

    def open_file():
        global filename, img
        f_types = [('Png files', '.png'), ('Jpg Files', '.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = ImageTk.PhotoImage(file=filename)
        b2 = Button(entries_frame, image=img)  # using Button
        b2.grid(row=6, column=2, padx=10, pady=5, sticky="w")  # display uploaded photo

    photo = Label(entries_frame, text='Upload Photo :', font=("Calibri", 12))
    photo.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    photobtn = Button(entries_frame, text='Choose File', command=lambda: open_file(), width=25)
    photobtn.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    lbls = Label(entries_frame, text="Employee Status :", font=("Calibri", 12))
    lbls.grid(row=6, column=3, padx=10, pady=5, sticky="w")
    list_of_CompanyStatus = ["Active", "Inactive"]
    status = StringVar()
    dropliststatus = OptionMenu(entries_frame, status, *list_of_CompanyStatus)
    dropliststatus.grid(row=6, column=4, padx=15, pady=15, sticky="w")
    dropliststatus.config(width=25)
    status.set('--Select--')

    def add_employee():
        global image, filename
        fob = open(filename, 'rb')  # filename from upload_file()
        #print(fob)
        fob = fob.read()
        print(fob)
        if ename.get() == "" or droplist_g.get() == "" or dob.get() == "" or age.get() == "" or mobile.get() == "" or hphone.get() == "" or txtAddress.get(1.0, END) == "" or txtAddress1.get(1.0, END) == "" or droplist_s.get() == "" or mail.get() == "" or doj.get() == "" or droplist_d.get() == "" or droplist_1.get() == "" or droplist_2.get() == "" or sal.get() == "" or fob =="" or status.get()=="":
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")

        if (len(hphone.get()) == 10 and hphone.get().isdigit() and len(
                mobile.get()) == 10 and mobile.get().isdigit()):
            messagebox.showinfo("Number Success", "This is 10 digit number")
        else:
            messagebox.showerror("Error in Input", "Please Fill 10 digit contact number")
            return

        if (len(age.get()) == 2 and age.get().isdigit() and len(sal.get()) <= 5 and sal.get().isdigit()):
            messagebox.showinfo("Age or Salary", "Data added Correct")
        else:
            messagebox.showerror("Error in Input", "Please Fill age=2 and salary<=5 digits")
            return

        DB.insertEmp(ename.get(), droplist_g.get(), dob.get(), age.get(), mobile.get(), hphone.get(),
                     droplist_s.get(),
                     txtAddress.get(1.0, END), txtAddress1.get(1.0, END), mail.get(), doj.get(), droplist_d.get(),
                     droplist_1.get(), droplist_2.get(), sal.get(), fob, status.get())
        messagebox.showinfo("Success", "Record Update")
        clearall()
        displayall()

    def update_employee():

        #photo = "image"
        if ename.get() == "" or droplist_g.get() == "" or dob.get() == "" or age.get() == "" or mobile.get() == "" or hphone.get() == "" or txtAddress.get(1.0, END) == "" or txtAddress1.get(1.0, END) == "" or droplist_s.get() == "" or mail.get() == "" or doj.get() == "" or droplist_d.get() == "" or droplist_1.get() == "" or droplist_2.get() == "" or sal.get() == "" or status.get()=="" :
            messagebox.showerror("Error in Input", "Please Fill All the Details")

        if (len(hphone.get()) == 10 and hphone.get().isdigit() and len(mobile.get()) == 10 and mobile.get().isdigit()):
            messagebox.showinfo("Number Success", "This is 10 digit number")
        else:
            messagebox.showerror("Error in Input", "Please Fill 10 digit contact number")
            return

        if(len(age.get()) == 2 and age.get().isdigit() and len(sal.get()) <= 5 and sal.get().isdigit()):
            messagebox.showinfo("Age or Salary", "Data added Correct")
        else:
            messagebox.showerror("Error in Input", "Please Fill age=2 and salary<=5 digits")
            return

        DB.updateEmp(row[0], ename.get(), droplist_g.get(), dob.get(), age.get(), mobile.get(), hphone.get(),
                         droplist_s.get(),
                         txtAddress.get(1.0, END), txtAddress1.get(1.0, END), mail.get(), doj.get(), droplist_d.get(),
                         droplist_1.get(), droplist_2.get(), sal.get(), status.get())
        messagebox.showinfo("Success", "Record Update")
        clearall()
        displayall()



    def getData(event):
        selected_row = new_emp.focus()
        data = new_emp.item(selected_row)
        global row
        row = data["values"]
        # print(row)
        ename.set(row[1])
        droplist_g.set(row[2])
        dob.set(row[3])
        age.set(row[4])
        mobile.set(row[5])
        hphone.set(row[6])
        droplist_s.set(row[7])
        txtAddress.delete(1.0, END)
        txtAddress.insert(END, row[8])
        txtAddress1.delete(1.0, END)
        txtAddress1.insert(END, row[9])
        mail.set(row[10])
        doj.set(row[11])
        droplist_d.set(row[12])
        droplist_1.set(row[13])
        droplist_2.set(row[14])
        sal.set(row[15])
        status.set(row[17])


    def delete_emp():
        DB.remove(row[0])
        clearall()
        displayall()

    def displayall():
        new_emp.delete(*new_emp.get_children())
        for row in DB.fetch():
            new_emp.insert("", END, values=row)

    def clearall():
        ename.set("")
        droplist_g.set("--Select--")
        dob.set("")
        age.set("")
        mobile.set("")
        hphone.set("")
        txtAddress.delete(1.0, END)
        txtAddress1.delete(1.0, END)
        droplist_s.set("--Select--")
        mail.set("")
        doj.set("")
        droplist_d.set("--Select--")
        droplist_1.set("--Select--")
        droplist_2.set("--Select--")
        sal.set("")
        status.set("--Select--")

    btn_frame = Frame(entries_frame)
    btn_frame.grid(row=7, column=0, columnspan=4, padx=0, pady=0, sticky="w")
    btnAdd = Button(btn_frame, command=add_employee, text="Add Record", width=15, font=("Calibri", 16, "bold"),
                    fg="white", bg="#16a085", bd=0).grid(row=0, column=2, padx=30, pady=60)
    btnUpdate = Button(btn_frame, command=update_employee, text="Update Record", width=15, font=("Calibri", 16, "bold"),
                      fg="white", bg="#2980b9", bd=0).grid(row=0, column=3, padx=30, pady=60)
    #btnDelete = Button(btn_frame, command=deleteall, text="Delete Record", width=15, font=("Calibri", 16, "bold"),
     #                 fg="white", bg="#c0392b", bd=0).grid(row=0, column=4, padx=30, pady=60)
    btnClear = Button(btn_frame, command=clearall, text="Clear Record", width=15, font=("Calibri", 16, "bold"),
                       fg="white", bg="#f39c12", bd=0).grid(row=0, column=5, padx=30, pady=60)

    # _________________Old Code ----------------------------

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()

    con.execute("SELECT * FROM Employee")
    # Table Frame
    tree_frame = Frame(new_emp, bg="#ecf0f1")
    tree_frame.place(x=0, y=470, width=1360, height=280)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tree_scroll1 = Scrollbar(tree_frame, orient='horizontal')
    tree_scroll1.pack(side=BOTTOM, fill=X)

    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 16), rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 14))  # Modify the font of the headings

    new_emp = ttk.Treeview(tree_frame, columns=(
        "Emp_ID", "Emp_Name", "Emp_Gender", "Emp_DOB", "Emp_Age", "Emp_Mobile", "Emp_Home_Contect",
        "Emp_Matiral_Status",
        "Emp_Address", "Emp_Parmanent_Add", "Emp_Email", "Emp_DOJ", "Emp_Designation", "Emp_Department",
        "Emp_Education",
        "Emp_Basic_Salary", "Emp_Photo", "Emp_Status"), style="mystyle.Treeview", yscrollcommand=tree_scroll.set,
                      xscrollcommand=tree_scroll1.set)

    tree_scroll.config(command=new_emp.yview)
    tree_scroll1.config(command=new_emp.xview)

    new_emp.column("Emp_ID", width=150, minwidth=155, anchor=CENTER)
    new_emp.column("Emp_Name", width=350, minwidth=310, anchor=CENTER)
    new_emp.column("Emp_Gender", width=150, minwidth=135, anchor=CENTER)
    new_emp.column("Emp_DOB", width=100, minwidth=135, anchor=CENTER)
    new_emp.column("Emp_Age", width=105, minwidth=125, anchor=CENTER)
    new_emp.column("Emp_Mobile", width=150, minwidth=160, anchor=CENTER)
    new_emp.column("Emp_Home_Contect", width=150, minwidth=160, anchor=CENTER)
    new_emp.column("Emp_Matiral_Status", width=150, minwidth=250, anchor=CENTER)
    new_emp.column("Emp_Address", width=450, minwidth=350, anchor=CENTER)
    new_emp.column("Emp_Parmanent_Add", width=450, minwidth=350, anchor=CENTER)
    new_emp.column("Emp_Email", width=150, minwidth=320, anchor=CENTER)
    new_emp.column("Emp_DOJ", width=100, minwidth=125, anchor=CENTER)
    new_emp.column("Emp_Designation", width=250, minwidth=250, anchor=CENTER)
    new_emp.column("Emp_Department", width=250, minwidth=250, anchor=CENTER)
    new_emp.column("Emp_Education", width=250, minwidth=250, anchor=CENTER)
    new_emp.column("Emp_Basic_Salary", width=150, minwidth=250, anchor=CENTER)
    new_emp.column("Emp_Photo", width=150, minwidth=250, anchor=CENTER)
    new_emp.column("Emp_Status", width=100, minwidth=250, anchor=CENTER)

    new_emp.heading("Emp_ID", text="Emp_ID", anchor=CENTER)
    new_emp.heading("Emp_Name", text="Emp_Name", anchor=CENTER)
    new_emp.heading("Emp_Gender", text="Emp_Gender", anchor=CENTER)
    new_emp.heading("Emp_DOB", text="Emp_DOB", anchor=CENTER)
    new_emp.heading("Emp_Age", text="Emp_Age", anchor=CENTER)
    new_emp.heading("Emp_Mobile", text="Emp_Mobile", anchor=CENTER)
    new_emp.heading("Emp_Home_Contect", text="Emp_Home_Content", anchor=CENTER)
    new_emp.heading("Emp_Matiral_Status", text="Emp_Matiral_Status", anchor=CENTER)
    new_emp.heading("Emp_Address", text="Emp_Address", anchor=CENTER)
    new_emp.heading("Emp_Parmanent_Add", text="Emp_Parmanent_Add", anchor=CENTER)
    new_emp.heading("Emp_Email", text="Emp_Email", anchor=CENTER)
    new_emp.heading("Emp_DOJ", text="Emp_DOJ", anchor=CENTER)
    new_emp.heading("Emp_Designation", text="Emp_Designation", anchor=CENTER)
    new_emp.heading("Emp_Department", text="Emp_Department", anchor=CENTER)
    new_emp.heading("Emp_Education", text="Emp_Education", anchor=CENTER)
    new_emp.heading("Emp_Basic_Salary", text="Emp_Basic_Salary", anchor=CENTER)
    new_emp.heading("Emp_Photo", text="Emp_Photo", anchor=CENTER)
    new_emp.heading("Emp_Status", text="Emp_Status", anchor=CENTER)

    new_emp['show'] = "headings"
    new_emp.bind("<ButtonRelease-1>", getData)
    new_emp.pack(expand="True", fill=X)
    displayall()
    new_emp.mainloop()
