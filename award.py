from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import Database as DB

def add_award(root):

    new_award = Toplevel(root)
    new_award.geometry("1920x1080+0+0")
    new_award.title('Awards')
    new_award.resizable(False, False)
    new_award.config()
    new_award.state("zoomed")

    title = Label(new_award, text='Company Awards', bg='lightpink', fg='Black', font=('calibri', 20, 'bold'), relief=GROOVE, anchor=CENTER, bd=5)
    title.pack(fill=X, ipady=2)

    #emp_id = StringVar()
    emp_name = StringVar()
    month = StringVar()
    year = StringVar()

    entries_frame = Frame(new_award)
    entries_frame.pack(side=TOP, fill=X)

    label_0 = Label(entries_frame, text="Department Name :", font=("bold", 10))
    label_0.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT dep_name FROM department")

    my_data = con.fetchall()
    my_list = [r for r, in my_data]  # create a  list
    droplist_1 = StringVar(entries_frame)
    droplist_1.set(my_list[0])  # default value
    droplist1 = OptionMenu(entries_frame, droplist_1, *my_list)
    droplist1.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    droplist1.config(width=25)
    droplist_1.set('--Select--')
    connect.close()

    label_0 = Label(entries_frame, text="Employee Name :", font=("bold", 10))
    label_0.grid(row=0, column=2, padx=10, pady=10, sticky="w")

    connect1 = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con1 = connect1.cursor()
    con1.execute("SELECT emp_name FROM employee")

    my_data1 = con1 .fetchall()
    my_list1 = [r for r, in my_data1]  # create a  list
    droplist_2 = StringVar(entries_frame)
    droplist_2.set(my_list1[0])  # default value
    droplist2 = OptionMenu(entries_frame, droplist_2, *my_list1)
    droplist2.grid(row=0, column=3, padx=10, pady=10, sticky="w")
    droplist2.config(width=25)
    droplist_2.set('--Select--')
    connect1.close()

    label_1 = Label(entries_frame, text="Award :", font=("bold", 10))
    label_1.grid(row=0, column=4, padx=10, pady=10, sticky="w")
    list_of_Department = ["Best Attendance Award", "Employee of the Month", "Best Team Player", "Forever With Us", "The Brainiac"]
    droplist_3 = StringVar()
    droplist = OptionMenu(entries_frame, droplist_3, *list_of_Department)
    droplist.config(width=20)
    droplist_3.set('--Select--')
    droplist.grid(row=0, column=5, padx=10, pady=10, sticky="w")

    label_3 = Label(entries_frame, text="For The Month :", font=("bold", 10))
    label_3.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_3 = Entry(entries_frame, textvariable=month, font=("bold", 10), width=30)
    entry_3.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    label_4 = Label(entries_frame, text="Year :", font=("bold", 10))
    label_4.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    entry_4 = Entry(entries_frame, textvariable=year, font=("bold", 10), width=30)
    entry_4.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    def getData(event):
        selected_row = new_award.focus()
        data = new_award.item(selected_row)
        global row
        row = data["values"]
        #print(row)
        droplist_1.set(row[1])
        droplist_2.set(row[2])
        droplist_3.set(row[3])
        month.set(row[4])
        year.set(row[5])

    def displayall():
        new_award.delete(*new_award.get_children())
        for row in DB.allAward():
            new_award.insert("", END, values=row)

    def add_awardee():
        if droplist_1.get() == "" or droplist_2.get() == "" or droplist_3.get() == "" or month.get() == "" or year.get() == "":
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")

        if (len(year.get()) == 4 and year.get().isdigit()):
            messagebox.showinfo("Number Success", "Correct format yyyy")
        else:
            messagebox.showerror("Error in Input", "Please enter year in number and must be 4 digit Details")
            return

        DB.insertAward(droplist_1.get(), droplist_2.get(), droplist_3.get(), month.get(), year.get())
        messagebox.showinfo("Success", "Record Inserted")
        displayall()
        clearall()

    def update_awardee():
        if droplist_1.get() == "" or droplist_2.get() == "" or droplist_3.get() == "" or month.get() == "" or year.get() == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
        if (len(year.get()) == 4 and year.get().isdigit()):
            messagebox.showinfo("Number Success", "Correct Year")
        else:
            messagebox.showerror("Error in Input", "Please enter year in number and must be 4 digit Details")
            return

        DB.updateAward(row[0], droplist_1.get(), droplist_2.get(), droplist_3.get(), month.get(), year.get())
        messagebox.showinfo("Success", "Record Update")
        displayall()
        clearall()

    def delete_awardee():
        DB.removeAward(row[0])
        displayall()
        clearall()

    def clearall():
        droplist_1.set("--Select--")
        droplist_2.set("--Select--")
        droplist_3.set("--Select--")
        month.set("")
        year.set("")

    btn_frame = Frame(entries_frame)
    btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
    btnAdd = Button(btn_frame, command=add_awardee, text="Add Details", width=15, font=("Calibri", 16, "bold"),
                fg="white", bg="#16a085", bd=0).grid(row=0, column=0, padx=10 , pady=40)
    btnEdit = Button(btn_frame, command=update_awardee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9", bd=0).grid(row=0, column=1, padx=10, pady=40)
    btnDelete = Button(btn_frame, command=delete_awardee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b", bd=0).grid(row=0, column=2, padx=10, pady=40)
    btnClear = Button(btn_frame, command=clearall, text="Clear Details", width=15, font=("Calibri", 16, "bold"),
                  fg="white", bg="#f39c12", bd=0).grid(row=0, column=3, padx=10, pady=40)

    #table Frame
    tree_frame = Frame(new_award, bg="#ecf0f1")
    tree_frame.place(x=0, y=400, width=1360, height=350)

    #Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tree_scroll1 = Scrollbar(tree_frame, orient='horizontal')
    tree_scroll1.pack(side=BOTTOM, fill=X)


    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings

    new_award = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll1.set, columns=(1, 2, 3, 4, 5, 6), style="mystyle.Treeview")

    tree_scroll.config(command=new_award.yview)
    tree_scroll1.config(command=new_award.xview)

    new_award.heading("1", text="Award ID")
    new_award.column("1", width=150, minwidth=355, anchor=CENTER)
    new_award.heading("2", text="Department Name")
    new_award.column("2", width=250, minwidth=350, anchor=CENTER)
    new_award.heading("3", text="Employee Name")
    new_award.column("3", width=250, minwidth=350, anchor=CENTER)
    new_award.heading("4", text="Award")
    new_award.column("4",width=250, minwidth=350, anchor=CENTER)
    new_award.heading("5", text="For the Month")
    new_award.column("5", width=200, minwidth=301, anchor=CENTER)
    new_award.heading("6", text="Year")
    new_award.column("6",  width=150, minwidth=155, anchor=CENTER)
    new_award['show'] = 'headings'
    new_award.bind("<ButtonRelease-1>", getData)
    new_award.pack(fill=X, pady=0)

    displayall()
    root.mainloop()
