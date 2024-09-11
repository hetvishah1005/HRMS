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

# o = Database("Department.db")
# o.insert("Training","Elena")
# # o.update('2','Project','Prachi')
# # o.remove('5')
# # o.remove('1')
# o.fetch()