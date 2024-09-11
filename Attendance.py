from tkinter import *
import tkinter
from tkinter import ttk
import datetime
from datetime import date, timedelta
import time
import mysql.connector
import Database as DB


def show_attend(root, uname):

    print(uname)
    data_attend = Toplevel(root)
    data_attend.geometry("1920x1080+0+0")
    data_attend.resizable(False, False)
    data_attend.config()
    data_attend.state("zoomed")
    data_attend.title('Attendance Record')

    connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con = connect.cursor()
    con.execute("SELECT * FROM attendance where emp_name='"+uname+"'")

    title = Label(data_attend, text='Attendance Record:', bg='#16a085', fg='white', font=('calibri', 20, 'bold'),
                  relief=GROOVE, anchor=W, bd=6, padx=10, pady=180)
    title.pack(fill=X, ipady=25)

    connect1 = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
    con1 = connect1.cursor()
    con1.execute("SELECT dep_name, emp_name FROM award ORDER BY aw_id DESC LIMIT 1")
    data = con1.fetchone()
    connect1.close()
    lblEM = Label(title, text=f"{data}", padx=10, font=("Calibri", 16, "bold"), fg="white", bg="#16a085", bd=0).pack(
        side=LEFT, padx=265, pady=0)

    date_and_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    dt = Label(title, text=f"{date_and_time}", padx=10, font=("Calibri", 16, "bold"), fg="white", bg="#16a085",
               bd=0).pack(side=RIGHT, padx=5, pady=0)

    # def displayall(uname):
    #     #tv_emp.delete(*data_atten.get_children())
    #     for rows in DB.fetch_all(uname):
    #         data_atten.insert('', END, values=rows)

    tree_frame = Frame(data_attend)
    tree_frame.place(x=0, y=95, width=1365, height=490)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tree_scroll1 = Scrollbar(tree_frame, orient='horizontal')
    tree_scroll1.pack(side=BOTTOM, fill=X)

    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 16), rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 14))  # Modify the font of the headings

    data_atten = ttk.Treeview(tree_frame, columns=(
        "Att_Id", "Emp_Id", "Emp_Name", "Att_Date", "Att_Intime", "Att_Outtime"), style="mystyle.Treeview",
                               yscrollcommand=tree_scroll.set,
                               xscrollcommand=tree_scroll1.set)

    tree_scroll.config(command=data_atten.yview)
    tree_scroll1.config(command=data_atten.xview)

    data_atten.column("Att_Id", width=150, minwidth=155, anchor=CENTER)
    data_atten.column("Emp_Id", width=350, minwidth=310, anchor=CENTER)
    data_atten.column("Emp_Name", width=150, minwidth=135, anchor=CENTER)
    data_atten.column("Att_Date", width=100, minwidth=135, anchor=CENTER)
    data_atten.column("Att_Intime", width=100, minwidth=135, anchor=CENTER)
    data_atten.column("Att_Outtime", width=105, minwidth=125, anchor=CENTER)

    data_atten.heading("Att_Id", text="Att_Id", anchor=CENTER)
    data_atten.heading("Emp_Id", text="Emp_Id", anchor=CENTER)
    data_atten.heading("Emp_Name", text="Emp_Name", anchor=CENTER)
    data_atten.heading("Att_Date", text="Att_Date", anchor=CENTER)
    data_atten.heading("Att_Intime", text="Att_Intime", anchor=CENTER)
    data_atten.heading("Att_Outtime", text="Att_Outtime", anchor=CENTER)
    #displayall(uname)
    i = 0
    for rows in con:
        data_atten.insert("", i, values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]))
        #data_atten.insert("", i, text=" ", values=(rows[2], rows[3], rows[4], rows[5]))
        i = i + 1
        #print(i)
    data_atten['show'] = "headings"
    data_atten.pack(expand="True", fill=X)
    connect.close()
    data_attend.mainloop()
