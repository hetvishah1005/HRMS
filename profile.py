# from tkinter import *
# from PIL import ImageTk, Image
# import mysql.connector
# import Database as DB
#
# def my_profile(root, uname):
#
#     prof = Toplevel(root)
#     prof.geometry("1920x1080+0+0")
#     prof.resizable(False, False)
#     prof.config()
#     prof.state("zoomed")
#     prof.title('My Profile')
#     print("THis is my profile page")
#     print(uname)
#     #frame ke under rakhna hai mainme as like we did in hr main
#     connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
#     con = connect.cursor()
#     #sql = "SELECT emp_id, emp_name, emp_gender, emp_dob, emp_mobile, emp_address, emp_doj, emp_designation, emp_department from employee where emp_email=%s"
#     sql = "SELECT * from employee"
#     #print(sql)
#     con.execute(sql)
#     rows = con.fetchall()
#     for row in rows:
#         if row[10] == uname:
#             print(row)
#             left_lbl = Label(prof, bg="pink", bd=0)
#             left_lbl.place(x=0, y=0, relheight=1, width=650)
#
#             right_lbl = Label(prof, bg="lightblue", bd=0)
#             right_lbl.place(x=650, y=0, relheight=1, relwidth=1)
#
#             label = Label(prof, relief=RIDGE, bd=8)
#             label.place(x=270, y=80, height=530, width=850)
#
#             title = Label(label, text="PROFILE",  font=("calibri", 30, "bold"), bg="lightblue", fg="white", padx=10, relief=GROOVE, anchor=CENTER, bd=5).place(x=0, y=0, relwidth=1)
#
#             image = Image.open(r"image/jeel.png")
#             img_resize = image.resize((110, 130))
#             img = ImageTk.PhotoImage(img_resize)
#             logo = Label(label, image=img)
#             logo.image = img
#             logo.pack(side=TOP, padx=40, pady=100)
#
#             name = Label(label, text="Name :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=250)
#             txt_name = Label(label, text=f"{row[1]}", font=("calibri", 15)).place(x=190, y=250)
#
#             e_id = Label(label, text="Employee Id :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=250)
#             txt_eid = Label(label, text=f"{row[0]}", font=("calibri", 15)).place(x=680, y=250)
#
#             email = Label(label, text="Email Id :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=300)
#             txt_email = Label(label, text=f"{row[6]}", font=("calibri", 15)).place(x=190, y=300)
#
#             phoneno = Label(label, text="Phone No :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=300)
#             txt_phoneno = Label(label, text=f"{row[4]}", font=("calibri", 15)).place(x=680, y=300)
#
#             dob = Label(label, text="Birth Date :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=350)
#             txt_dob = Label(label, text=f"{row[3]}", font=("calibri", 15)).place(x=190, y=350)
#
#             gender = Label(label, text="Gender :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=350)
#             txt_gender = Label(label, text=f"{row[2]}", font=("calibri", 15), bd=2).place(x=680, y=350)
#
#             Address = Label(label, text="Address :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=400)
#             txt_address = Label(label, text=f"{row[5]}", font=("calibri", 15)).place(x=190, y=400)
#
#             doj = Label(label, text="Joining Date :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=400)
#             txt_doj = Label(label, text=f"{row[7]}", font=("calibri", 15)).place(x=680, y=400)
#
#             dep = Label(label, text="Department :", font=("calibri", 15, "bold"), fg="Black").place(x=60, y=450)
#             txt_dep = Label(label, text=f"{row[9]}", font=("calibri", 15)).place(x=190, y=450)
#
#             des = Label(label, text="Designation :", font=("calibri", 15, "bold"), fg="Black").place(x=520, y=450)
#             txt_des = Label(label, text=f"{row[8]}",  font=("calibri", 15)).place(x=680, y=450)
#     connect.close()
#     prof.mainloop()
