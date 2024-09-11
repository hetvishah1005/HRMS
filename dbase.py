import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS List_Of_Department 
            (department_id Integer PRIMARY KEY,
            department_name TEXT,
            department_head TEXT)"""

        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, department_name, department_head):
        self.cur.execute("insert into List_Of_Department values(NULL,?,?)", (department_name, department_head))
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * from List_Of_department")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from List_Of_Department where department_id=?", (id,))
        self.conn.commit()

    def update(self, id, department_name, department_head):
        self.cur.execute("update List_Of_Department set department_name=?, department_head=? where department_id=?",
        (department_name, department_head, id))
        self.conn.commit()


class Awardees:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS Awardee 
            (Emp_id Integer PRIMARY KEY,
            emp_name TEXT,
            droplist_2 TEXT,
            month TEXT,
            year int)"""

        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, emp_name, droplist_2, month, year):
        self.cur.execute("insert into Awardee values(NULL,?,?,?,?)", (emp_name, droplist_2, month, year))
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * from Awardee")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    # Delete a Record in dbase
    def remove(self, id):
        self.cur.execute("delete from Awardee where emp_id=?", (id,))
        self.conn.commit()

    def update(self, id, emp_name, droplist_2, month, year):
        self.cur.execute("update Awardee set emp_name=?, droplist_2=?, month=?, year=? where emp_id=?",
             (emp_name, droplist_2, month, year, id))
        self.conn.commit()


class Leave_request:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS Requests 
            (emp_id Integer PRIMARY KEY,
            name TEXT,
            droplist_5 TEXT,
            leave_typ TEXT,
            date TEXT
            fdate TEXT
            morn TEXT
            after TEXT
            droplist_4 TEXT
            con TEXT
            mail TEXT
            var1 TEXT
            reason TEXT)"""

        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, name, droplist_5, leave_typ, date, fdate, morn, after, droplist_4, con, mail, var1, reason):
        self.cur.execute("insert into Requests values(NULL,?,?,?,?,?,?,?,?,?,?,?,?)", (name, droplist_5, date, leave_typ, con, mail, fdate, morn, after, droplist_4, var1, reason))
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * from Requests")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    #  # Delete a Record in DB
    # def remove(self, id):
    #     self.cur.execute("delete from Requests where emp_id=?", (id,))
    #     self.conn.commit()
    #
    # def update(self, id, name, droplist_5, leave_typ, date):
    #     self.cur.execute("update Requests set name=?, droplist_5=?, leave_typ=?, date=? where emp_id=?",
    #          (name, droplist_5, date, leave_typ, con, mail, fdate, morn, after, droplist_4, var1, reason, id))
    #     self.conn.commit()


class Employees:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        sql = """
           CREATE TABLE IF NOT EXISTS Employee
                (emp_id Integer PRIMARY KEY,
                name TEXT,
                droplist_g TEXT,
                dob TEXT,
                age TEXT,
                contact TEXT,
                phone TEXT,
                address TEXT,
                address1 TEXT,
                droplist_s TEXT,
                mail TEXT,
                doj TEXT,
                design TEXT,
                droplist_1 TEXT,
                droplist_2 TEXT,
                sal TEXT)"""

        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, name, droplist_g, dob, age, contact, phone,  address, address1, droplist_s, mail, doj, design, droplist_1, droplist_2, sal):
        self.cur.execute("insert into Employee values (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, contact, mail, droplist_1, design, doj, sal, droplist_g, dob, age, phone, address, address1, droplist_s, droplist_2))
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * from Employee")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from Employee where emp_id=?", (id,))
        self.conn.commit()

    def update(self, id, name, droplist_g, dob, age, contact, phone,  address, address1, droplist_s, mail, doj, design, droplist_1, droplist_2, sal):
        self.cur.execute(
            "update Employee set name=?, droplist_g=?, dob=?, age=?, contact=?, phone=?, address=?, address1=?, droplist_s=?, mail=?, doj=?, design=?, droplist_1=?, droplist_2=?, sal=? where emp_id=?",
            (name, contact, mail, droplist_1, design, doj, sal, droplist_g, dob, age, phone, address, address1, droplist_s, droplist_2, id))
        self.conn.commit()
