from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import Database as DB
connect = mysql.connector.connect(host="localhost", user='root', passwd='', database='ems', port='3306')
con = connect.cursor()
import main as HR
import empmain as emp

class Login_System:

    def __init__(self, root):
        self.login = master
        self.login.title('Login Page')
        self.login.geometry('1920x1080+0+0')
        self.login.resizable(False, False)
        self.login.config(bg="#fafafa")
        self.login.state("zoomed")

    # toplevel hoga class nikaldo
    #     self.login = Toplevel(root)
    #     self.login.title('Login Page')
    #     self.login.geometry("1920x1080+0+0")
    #     self.login.resizable(False, False)
    #     self.login.config()
    #     self.login.state("zoomed")

        image = Image.open("image/iphone.png")
        img_resize = image.resize((400, 500))
        img = ImageTk.PhotoImage(img_resize)
        image = Label(self.login, image=img, bg="white", bd=0)
        image.image = img
        image.pack(anchor='w', padx=200, pady=40)

        lg_frame = Frame(self.login, bd=2,bg="rosybrown1", relief=RIDGE)
        lg_frame.place(x=630, y=70, width=350, height=450)

        self.title = Label(lg_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="rosybrown3",
                       fg="deeppink4").place(x=0, y=0, relwidth=1, height=90)

        self.uname = Label(lg_frame, text="USER NAME", font=("times new roman", 18, "bold"),bg="rosybrown1", fg="grey34").place(
            x=100, y=110)
        self.username = StringVar()
        self.txt_uname = Entry(lg_frame, textvariable=self.username, font=("times new roman", 15), fg="green", bd=2).place(
            x=75, y=150)

        self.password = Label(lg_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="rosybrown1", fg="grey34").place(
            x=110, y=190)
        self.password = StringVar()
        self.txt_password = Entry(lg_frame, textvariable=self.password, font=("times new roman", 15), fg="green", bd=2,
                              show='*').place(x=75, y=230)

        self.btn = Button(lg_frame, text="Forgot Password?", font=("times new roman", 15), bg="rosybrown1", bd=0, fg="#B00857",
                      command=None).place(x=110, y=290)

        self.btn1 = Button(lg_frame, command=lambda: self.check(), text="Login", font=("times new roman", 18, "bold"),
                       bg="white", fg="#B00857").place(x=140, y=350)

        self.img1 = ImageTk.PhotoImage(file="image/girl.png")
        self.img2 = ImageTk.PhotoImage(file="image/man&woman.png")
        self.img3 = ImageTk.PhotoImage(file="image/man&woman.png")

        self.lbl_change_image = Label(self.login, bg="grey")
        self.lbl_change_image.place(x=362, y=104, width=219, height=374)

        self.animate()


    def animate(self):
        self.image = self.img1
        self.img1 = self.img2
        self.img2 = self.img3
        self.img3 = self.image
        self.lbl_change_image.config(image=self.image)
        self.lbl_change_image.after(2000, self.animate)


    def check(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All field are Requires!")
        else:
            uname = self.username.get()
            passwd = self.password.get()
            row = DB.loginCheck(uname, passwd)
            print(row)
            if row:
                if row[4] == "admin":
                    messagebox.showinfo("Success", "Welcome To HR Management System!")
                    HR.main(row)
                elif row[4] == 'employee':
                    messagebox.showinfo("Success", f"Welcome  {row[1]}")
                    emp.main(row[1])
                else:
                    messagebox.showerror("Error", "Invalid Username and Password!")
            else:
                messagebox.showerror("Error", "Invalid Username and Password!")
            # for row in DB.loginCheck():
            #     if row[1] == uname and row[2] == passwd and row[3] == "admin":
            #         messagebox.showinfo("Information", "Welcome To HR Management System!")
            #         HR.main()
            #     # toplevelwindow.destroy login.destroy
            #     if row[1] == uname and row[2] == passwd and row[3] == "employee":
            #     # insert query add karni hai jiska login hoga uski details add hogi
            #         emp.main(row)
            #     # toplevelwindow.destroy login.destroy
            #         messagebox.showinfo("Information", f"Welcome to Employee - {row[1]}")
            #     else:
            #         messagebox.showerror("Error", "Invalid Username and Password!")
master = Tk()
obj = Login_System(master)

master.mainloop()
