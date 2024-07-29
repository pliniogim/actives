import sqlite3


class ActivesDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('assets/database/actives.db')
        self.cursor = self.conn.cursor()

# connect database
    def database_init(self):
        print("#+connect_database")
        # create a table (if it doesn't exist)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS actives 
        (act_id INTEGER PRIMARY KEY AUTOINCREMENT,
        active_name TEXT)''')
        print("#-connect_database")
        self.conn.commit()

    # create an active
    def create_actives(self, act_id, name):
        print("#+create_actives")
        self.cursor.execute("INSERT INTO actives(act_id, active_name) VALUES (?,?)", (act_id, name))
        self.conn.commit()
        print("#-create_actives")

    def read_actives(self):
        print("#+read_actives")
        self.cursor.execute("SELECT * FROM actives")
        actives = self.cursor.fetchall()
        print("#-read_actives")

    def update_actives(self, act_id, new_name):
        print("#+update_actives")
        self.cursor.execute("UPDATE actives SET active_name = ? WHERE act_id = ?", (new_name, act_id))
        self.conn.commit()
        print("#-update_actives")

    def delete_actives(self, act_id):
        print("#+delete_actives")
        act_id = int(act_id)
        self.cursor.execute("DELETE FROM actives WHERE act_id = ?", (act_id, ))
        self.conn.commit()
        print("#-delete_actives")
