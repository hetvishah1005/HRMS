# Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def listofHoliday(root):
    list_holiday = Toplevel(root)
    list_holiday.geometry("1920x1080+0+0")
    list_holiday.title('Holiday List')
    list_holiday.resizable(False, False)
    list_holiday.config()
    list_holiday.state("zoomed")

    s = ttk.Style()
    s.theme_use('clam')

    image = Image.open(".\image\happy-holidays-WEB.png")
    img_resize = image.resize((1366, 650))
    img = ImageTk.PhotoImage(img_resize)
    label = Label(list_holiday, image=img)
    # label.image = img
    label.place(x=0, y=0)


    # Add a Treeview widget
    tree = ttk.Treeview(list_holiday, column=("c1", "c2", "c3", "c4"), show='headings', height=12)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Sr No.")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Holiday Name")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Date & Month")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Leave Type")


    # Insert the data in Treeview widget
    tree.insert('', 'end', text="1", values=('1', 'Makara Sankranti', '14 January', 'Regional Holiday'))
    tree.insert('', 'end', text="2", values=('2', 'Indian Republic Day', '26 January', 'National Holiday'))
    tree.insert('', 'end', text="3", values=('3', 'Holi Festival', 'March(1-2 day)', 'Public Holiday'))
    tree.insert('', 'end', text="4", values=('4', 'Ram Navami', '1 Day(on date)', 'Regional Holiday'))
    tree.insert('', 'end', text="5", values=('5', 'Independence Day', '15 August', 'National Holiday'))
    tree.insert('', 'end', text="6", values=('6', 'Raksha Bandhan', '1 Day or'
                                                                'half-day(on date)', 'Public Holiday'))
    tree.insert('', 'end', text="7", values=('7', 'Janmashtami', '1 Day(on date)', 'Regional Holiday'))
    tree.insert('', 'end', text="8", values=('8', 'Ganesh Chaturthi', '1 Day(on date)', 'Regional Holiday'))
    tree.insert('', 'end', text="9", values=('9', 'Gandhi jayanti', '02 October', 'National Holiday'))
    tree.insert('', 'end', text="10", values=('10', 'Durga Puja/Dussehra', '1 Day(on date)', 'Regional Holiday'))
    tree.insert('', 'end', text="11", values=('11', 'Diwali', '1 Day(on date)', 'Public Holiday'))
    tree.insert('', 'end', text="12", values=('12', 'Chirstmas', '25 December', 'Public Holiday'))

    tree.pack(pady=200)
    list_holiday.mainloop()

def add_Holiday(root):
    pass