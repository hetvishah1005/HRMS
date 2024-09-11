from tkinter import *
from tkinter import messagebox, ttk
import os
import time
import tempfile
import mysql.connector
import Database as DB

def add_payroll(root):

    new_pay = Toplevel(root)
    new_pay.geometry("1920x1080+0+0")
    new_pay.title('Employee Payroll')
    new_pay.config(bg='white')
    new_pay.state("zoomed")
    new_pay.resizable(False, False)

    title = Label(new_pay, text="Employee Payroll", font=("calibri", 30, "bold"), bg="lightblue", fg="white",
                  padx=10, relief=GROOVE, anchor=CENTER, bd=5).place(x=0, y=0, relwidth=1)

#============================Frame1=====================================
#========================variables=======================================
    global empId
    var_emp_id = StringVar()
    var_name = StringVar()
    var_dob = StringVar()
    var_gender = StringVar()
    var_doj = StringVar()
    var_contact = StringVar()
    var_email = StringVar()
    var_design = StringVar()
    var_depart = StringVar()
    var_addr = StringVar()
    var_medical = StringVar()
    var_convence = StringVar()
    var_basic_sal = StringVar()

    def printinput(*args):
        empId = var_emp_id.get()
        row = DB.getPayroll(empId)
        if row == " ":
            messagebox.showerror("error in salary section", "please enter iD properly")
        else:
            #print(row)
            var_name.set(row[1])
            var_dob.set(row[3])
            var_design.set(row[8])
            var_depart.set(row[9])
            var_gender.set(row[2])
            var_contact.set(row[5])
            var_email.set(row[7])
            var_addr.set(row[6])
            #var_addr.delete(1.0, END)
            #var_addr.insert(END, row[6])
            var_doj.set(row[4])
            var_basic_sal.set(row[10])
            #var_month.set("April")
            #var_year.set("2022")
            #var_total_day.set("31")
            #var_total_leave.set("3")
            var_medical.set("500")
            #var_pf.set("PF")
            var_convence.set("100")
            #var_net_sal.set("New Salary")
            #file_ = open("Salary_reciept/" + str(txt_sal_reciept.insert(END, new_sample)) + ".txt", 'r')

    frame1 = Frame(new_pay, bd=2, relief=RIDGE)
    frame1.place(x=5, y=60, width=655, height=680)
    title = Label(frame1, text="Employee Details", font=("calibri", 20), bg="lightblue", fg="black", padx=10).place(x=0, y=0, relwidth=1)

    lbl_id = Label(frame1, text="Employee Id :", font=("calibri", 12), fg="black").place(x=120, y=70)
    txt_id = Entry(frame1, textvariable=var_emp_id , font=("calibri", 12), fg="black").place(height=25, x=250, y=75)
    var_emp_id.trace("w", printinput)

    btn_search = Button(frame1, text="Search", command= lambda: (printinput()), font=("calibri", 12), fg="black", bg="lightgrey").place(x=470, y=70)

    lbl_name = Label(frame1, text="Name :", font=("calibri", 12), fg="black").place(x=10, y=150)
    txt_name = Entry(frame1, textvariable = var_name, font=("calibri", 12), fg="black").place(height=25, x=120, y=155)

    lbl_dob = Label(frame1, text="D.O.B :", font=("calibri", 12), fg="black").place(x=340, y=150)
    txt_dob = Entry(frame1, textvariable = var_dob,  font=("calibri", 12), fg="black").place(height=25, x=470, y=155)

    lbl_gender = Label(frame1, text="Gender :", font=("calibri", 12), fg="black").place(x=10, y=200)
    txt_gender = Entry(frame1, textvariable = var_gender,   font=("calibri", 12), fg="black").place(height=25, x=120, y=205)

    lbl_age = Label(frame1, text="D.O.J :", font=("calibri", 12), fg="black").place(x=340, y=200)
    txt_age = Entry(frame1, textvariable = var_doj,   font=("calibri", 12), fg="black").place(height=25, x=470, y=205)

    lbl_cont = Label(frame1, text="Contact No. :", font=("calibri", 12), fg="black").place(x=10, y=250)
    txt_cont = Entry(frame1, textvariable = var_contact, font=("calibri", 12), fg="black").place(height=25, x=120, y=255)

    lbl_mail = Label(frame1, text="Email :", font=("calibri", 12), fg="black").place(x=340, y=250)
    txt_mail = Entry(frame1, textvariable = var_email, font=("calibri", 12), fg="black").place(height=25, x=470, y=255)

    lbl_design = Label(frame1, text="Designation :", font=("calibri", 12), fg="black").place(x=10, y=300)
    txt_design = Entry(frame1, textvariable = var_design, font=("calibri", 12), fg="black").place(height=25, x=120, y=305)

    lbl_depart = Label(frame1, text="Department :", font=("calibri", 12), fg="black").place(x=340, y=300)
    txt_depart = Entry(frame1, textvariable = var_depart, font=("calibri", 12), fg="black").place(height=25, x=470, y=305)

    lbl_addr = Label(frame1, text="Address :", font=("calibri", 12), fg="black").place(x=10, y=350)
    txt_addr = Entry(frame1, textvariable = var_addr, font=("calibri", 12), fg="black").place(width=510, height=125, x=120, y=355)


# ==============================Frame2==================================
#=========================variables=====================================
    var_month = StringVar()
    var_year = StringVar()
    var_basic_sal = StringVar()
    var_total_day = StringVar()
    var_total_leave = StringVar()
    var_medical = StringVar()
    var_pf = StringVar()
    var_convence = StringVar()
    var_net_sal = StringVar()

    frame2 = Frame(new_pay, bd=2, relief=RIDGE)
    frame2.place(x=665, y=60, width=700, height=290)

    title = Label(frame2, text="Employee Salary Details", font=("calibri", 20), bg="lightblue", fg="black", padx=10).place( x=0, y=0, relwidth=1)

    lbl_mon = Label(frame2, text="Month :", font=("calibri", 12), fg="black").place(x=10, y=70)
    txt_mon = Entry(frame2, textvariable = var_month, font=("calibri", 12), fg="black").place(width=95, height=25, x=86, y=75)

    lbl_year = Label(frame2, text="Year :", font=("calibri", 12), fg="black").place(x=190, y=70)
    txt_year = Entry(frame2, textvariable = var_year, font=("calibri", 12), fg="black").place(width=95, height=25, x=248, y=75)

    lbl_sal = Label(frame2, text="Basic Salary :", font=("calibri", 12), fg="black").place(x=352, y=70)
    txt_sal = Entry(frame2, textvariable = var_basic_sal, font=("calibri", 12), fg="black").place(width=95, height=25, x=470, y=75)

    lbl_days = Label(frame2, text="Total Days :", font=("calibri", 12), fg="black").place(x=10, y=110)
    txt_days = Entry(frame2, textvariable = var_total_day, font=("calibri", 12), fg="black").place(width=100, height=25, x=120, y=115)

    lbl_absent = Label(frame2, text="Total Leaves :", font=("calibri", 12), fg="black").place(x=250, y=110)
    txt_absent = Entry(frame2, textvariable = var_total_leave, font=("calibri", 12), fg="black").place(width=100, height=25, x=400, y=115)

    lbl_medi = Label(frame2, text="Medical :", font=("calibri", 12), fg="black").place(x=10, y=150)
    txt_medi = Entry(frame2, textvariable = var_medical, font=("calibri", 12), fg="black").place(width=100, height=25, x=120, y=155)

    lbl_pf = Label(frame2, text="Provident Fund :", font=("calibri", 12), fg="black").place(x=250, y=150)
    txt_pf = Entry(frame2, textvariable = var_pf, font=("calibri", 12), fg="black").place(width=100, height=25, x=400, y = 155)

    lbl_cenvence = Label(frame2, text="Convence :", font=("calibri", 12), fg="black").place(x=10, y=190)
    txt_convence = Entry(frame2, textvariable = var_convence, font=("calibri", 12), fg="black").place(width=100, height=25, x=120, y=195)

    lbl_netsal = Label(frame2, text="Net Salary :", font=("calibri", 12), fg="black").place(x=250, y=190)
    txt_netsal = Entry(frame2, textvariable = var_net_sal, font=("calibri", 12), fg="black").place(width=100, height=25, x=400, y=195)

    btn_calculate = Button(frame2, text="Calculate", command=lambda: (calculate()), font=("calibri", 12), fg="black", bg = "orange").place(width=100, x=100, y=240)
    btn_save = Button(frame2, text="Save", command=lambda: (addSalary()), font=("calibri", 12), fg="black", bg="lightGreen").place(width=100, x=250, y=240)
    btn_clear = Button(frame2, text="Clear", command=lambda: (clearsal()), font=("calibri", 12), fg="black", bg="lightgrey").place(width=100, x=400, y=240)
        # ===========Frame3========================
    frame3 = Frame(new_pay, bd=2, relief=RIDGE)
    frame3.place(x=665, y=355, width=700, height=385)

    sal_frame = Frame(frame3, bg="white", bd=2, relief=RIDGE)
    sal_frame.place(x=0, y=0, width=695, height=385)
    title_sal = Label(sal_frame, text="Salary Reciept", font=("calibri", 16), bg="lightblue", fg="black", padx=10)
    title_sal.place(x=0, y=0, relwidth=1)
    sal_frame2 = Frame(sal_frame, bg="white", bd=1, relief=RIDGE)
    sal_frame2.place(x=0, y=30, relwidth=1, height=385)

    sample = f'''\t Company Name: Gujarat Infotech Limited 
            -------------------------------------------------------------------
            Employee Id\t\t: 
            Salary Of\t\t:  Mon-YYYY
            Generated On\t\t\t : DD-MM-YYYY
            -------------------------------------------------------------------
            Total Days\t\t    : DD
            Total Present\t\t : DD
            Total Leaves\t\t  : DD
            Convence\t\t      : Rs._______
            Medical\t\t       : Rs._______
            PF\t\t\t          : Rs._______
            Gross Payment\t\t : Rs._______
            Net Salary\t\t    : Rs._______
            -------------------------------------------------------------------
            This is Computer generated slip,
            not required any Signature
            '''
    scroll_y = Scrollbar(sal_frame2, orient=VERTICAL)
    scroll_y.pack(fill=Y, side=RIGHT)

    txt_sal_reciept = Text(sal_frame2, font=("calibri", 16), yscrollcommand=scroll_y.set)
    txt_sal_reciept.pack(fill=BOTH, expand=1)
    scroll_y.config(command=txt_sal_reciept.yview)
    txt_sal_reciept.insert(END, sample)

    btn_print = Button(sal_frame2, text="Print", font=("calibri", 12), fg="black", bg="orange").place(width=80, x=540, y=300)

    def calculate():

        per_day = int(var_basic_sal.get()) / int(var_total_day.get())
        #print(per_day)
        work_day = int(var_total_day.get()) - int(var_total_leave.get())
        #print(work_day)
        sal_ = per_day * work_day
        bs = int(var_basic_sal.get())
        pf = int((bs * 12) / 100)
        #print(pf)
        var_pf.set(pf)
        deduct = int(var_medical.get()) + int(pf)
        addition = int(var_convence.get())
        net_sal = sal_ - deduct + addition
        var_net_sal.set(str(round(net_sal, 2)))

        # ================UPDATE RECIEPT==========================================
        new_sample = f'''\t Company Name, Gujarat Infotech Limited
        ------------------------------------------------
        Employee Id\t\t   : {var_emp_id.get()}
        Salary Of\t\t     :  {var_month.get()} - {var_year.get()}
        Generated On\t\t  : {str(time.strftime("%d-%m-%Y"))}
        --------------------------------------------------
        Total Days\t\t    : {var_total_day.get()}
        Total Present\t\t : {str(int(var_total_day.get())-int(var_total_leave.get()))}
        Total Leaves\t\t  :  {var_total_leave.get()}
        Convence\t\t      : Rs.{var_convence.get()}
        Medical\t\t       : Rs.{var_medical.get()}
        PF\t\t\t          : Rs.{var_pf.get()}
        Gross Payment\t\t : {var_basic_sal.get()}
        Net Salary\t\t    : {var_net_sal.get()}
        ------------------------------------------------
        This is Computer generated slip,
        not required any Signature
        '''
        txt_sal_reciept.delete('1.0', END)
        txt_sal_reciept.insert(END, new_sample)

    def addSalary():
        var_emp_id.get(),
        var_name.get(),
        var_dob.get(),
        var_gender.get(),
        var_doj.get(),
        var_contact.get(),
        var_email.get(),
        var_addr.get(),
        var_design.get(),
        var_depart.get(),
        var_month.get(),
        var_year.get(),
        var_basic_sal.get(),
        var_total_day.get(),
        var_total_leave.get(),
        var_medical.get(),
        var_pf.get(),
        var_convence.get(),
        var_net_sal.get(),
        #txt_addr.get('1.0', END),
        var_emp_id.get() + ".txt"
        file = open("Salary_reciept/"+str(var_emp_id.get())+".txt", "w")
        file.write(txt_sal_reciept.get('1.0', END))
        file.close()

        # if (len(var_year.get()) == 4 and var_year.get().isdigit() and len(
        #         var_total_leave.get()) <= 2  and  var_total_leave.get().isdigit()):
        #     messagebox.showinfo("Number Success", "Number is 10 digit number")
        # else:
        #     messagebox.showerror("Error in Input", "Please Fill 10 digit the Details")
        #     return
        #empId, empName, empDob, empDender, empDesignation, empDepartment, empMobile, empEmail, empAddress, empDoj, empBasicSalary, salMonth, salYear, totalDays, totalLeaves, esic, pf, convance, netPay
        DB.insertSalary(var_emp_id.get(), var_name.get(), var_dob.get(), var_gender.get(), var_design.get(), var_depart.get(), var_contact.get(), var_email.get(), var_addr.get(), var_doj.get(), var_basic_sal.get(), var_month.get(), var_year.get(), var_total_day.get(), var_total_leave.get(), var_medical.get(), var_pf.get(), var_convence.get(), var_net_sal.get())

    def clearsal():
        var_emp_id.set(""),
        var_name.set(""),
        var_dob.set(""),
        var_gender.set(""),
        var_doj.set(""),
        var_contact.set(""),
        var_email.set(""),
        var_addr.set(""),
        var_design.set(""),
        var_depart.set(""),
        var_month.set(""),
        var_year.set(""),
        var_basic_sal.set(""),
        var_total_day.set(""),
        var_total_leave.set(""),
        var_medical.set(""),
        var_pf.set(""),
        var_convence.set(""),
        var_net_sal.set(""),
        #var_emp_id.set() + ".txt"

    new_pay.mainloop()
