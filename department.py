from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Database as DB

def add_department(root):

    new_dep = Toplevel(root)
    new_dep.geometry("1920x1080+0+0")
    new_dep.title('Department')
    new_dep.resizable(False, False)
    new_dep.config()
    new_dep.state("zoomed")

    title = Label(new_dep, text='Departments', bg='lightpink', fg='Black', font=('calibri', 20, 'bold'), relief=GROOVE, anchor=CENTER, bd=5)
    title.pack(fill=X, ipady=2)

    department_name = StringVar()
    department_head = StringVar()

    def getData(event):
        selected_row = tv_dep.focus()
        data = tv_dep.item(selected_row)
        global row
        row = data["values"]
        # print(row)
        department_name.set(row[1])
        department_head.set(row[2])

    def displayall():
        tv_dep.delete(*tv_dep.get_children())
        for rows in DB.allDepartment():
            tv_dep.insert('', END, values=rows)

    def add_department():
        if department_name.get() == "" or department_head.get() == "":
            messagebox.showerror("Error in Input", "please fill  the details ")
            return
        DB.insertDepartment(department_name.get(), department_head.get())
        messagebox.showinfo("Success", "Record Inserted")
        clearall()
        displayall()

    def update_department():
        if department_name.get() == "" or department_head.get() == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        DB.updateDepartment(row[0], department_name.get(), department_head.get())
        messagebox.showinfo("Success", "Record Update")
        clearall()
        displayall()

    def delete_department():
        DB.removeDemartment(row[0])
        clearall()
        displayall()

    def clearall():
        department_name.set("")
        department_head.set("")

    entry_frame = Frame(new_dep)
    entry_frame.pack(side=TOP, fill="both", anchor=CENTER)
    label_1 = Label(entry_frame, text="Department Name :", width=14, font=("bold", 10))
    label_1.grid(row=0, column=0, padx=5, pady=10)

    entry_1 = Entry(entry_frame, textvariable=department_name, width=30)
    entry_1.grid(row=0, column=1, padx=5, pady=10)

    label_2 = Label(entry_frame, text="Department Head :", width=14, font=("bold", 10))
    label_2.grid(row=1, column=0, padx=5, pady=10)
    entry_2 = Entry(entry_frame, textvariable=department_head, width=30)
    entry_2.grid(row=1, column=1, padx=5, pady=10)

    btn_frame = Frame(entry_frame)
    btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
    btnAdd = Button(btn_frame, command=add_department, text="Add Details", width=15, font=("Calibri", 16, "bold"),
                fg="white", bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_department, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9", bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_department, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b", bd=0).grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearall, text="Clear Details", width=15, font=("Calibri", 16, "bold"),
                  fg="white", bg="#f39c12", bd=0).grid(row=0, column=3, padx=10)

    # Treeview Scrollbar
    tree_scroll = Scrollbar(new_dep)
    tree_scroll.pack(side=RIGHT, fill='y')

    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),
                    rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    tv_dep = ttk.Treeview(new_dep, yscrollcommand=tree_scroll.set, columns=(1, 2, 3), style="mystyle.Treeview")

    tree_scroll.config(command=tv_dep.yview)

    tv_dep.heading("1", text="Department Id")
    tv_dep.column("1", width=2, anchor=CENTER)
    tv_dep.heading("2", text="Department Name ")
    tv_dep.column("2", width=10, anchor=CENTER)
    tv_dep.heading("3", text="Department Head")
    tv_dep.column("3", width=3, anchor=CENTER)
    tv_dep['show'] = 'headings'
    tv_dep.bind("<ButtonRelease-1>", getData)
    tv_dep.pack(fill=X, pady=10)

    displayall()
    new_dep.mainloop()
