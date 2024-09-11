from tkinter import *

root = Tk()
root.title('Forgot Password')
root.geometry('1366x768')

def fpass(root):
    left_lbl = Label(root, bg="#08A3D2", bd=0)
    left_lbl.place(x=0, y=0, relheight=1, width=650)

    right_lbl = Label(root, bg="#031F3C", bd=0)
    right_lbl.place(x=650, y=0, relheight=1, relwidth=1)

    up_lbl = Label(root, bg="white", relief=GROOVE, bd=5)
    up_lbl.place(x=350, y=10, height=300, width=600)

    title = Label(up_lbl, text="Forgot Password", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(
        x=160, y=20)

    email = Label(up_lbl, text="Email", font=("times new roman", 18, "bold"), bg="white", fg="grey").place(x=270, y=100)
    txt_email = Entry(up_lbl, font=("times new roman", 15), bd=2).place(x=200, y=130)

    phoneno = Label(up_lbl, text="Phone No", font=("times new roman", 18, "bold"), bg="white", fg="grey").place(x=250,
                                                                                                                y=170)
    txt_phoneno = Entry(up_lbl, font=("times new roman", 15), bd=2).place(x=200, y=200)

    btn = Button(up_lbl, text="OK", font=("times new roman", 15, "bold"), bg="white", fg="#B00857").place(x=280, y=240)

    down_lbl = Label(root, bg='white', relief=GROOVE, bd=5)
    down_lbl.place(x=350, y=330, height=300, width=600)

    title1 = Label(down_lbl, text="Enter A New Password", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=110, y=20)

    password = Label(down_lbl, text="New Password", font=("times new roman", 18, "bold"), bg="white", fg="grey").place(x=240, y=100)
    txt_password = Entry(down_lbl, font=("times new roman", 15), bd=2).place(x=210, y=130)

    repass = Label(down_lbl, text="Confirm Password", font=("times new roman", 18, "bold"), bg="white",
                   fg="grey").place(x=215, y=170)
    txt_repass = Entry(down_lbl, font=("times new roman", 15), bd=2).place(x=210, y=200)

    btn1 = Button(down_lbl, text="OK", font=("times new roman", 15, "bold"), bg="white", fg="#B00857").place(x=290,y=240)

fpass(root)

root.mainloop()