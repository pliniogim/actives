import sqlite3
import datetime as dt
import traceback
import sys


# log database function error
def log_err(er):
    exc_type, exc_value, exc_tb = sys.exc_info()
    trcbck = traceback.format_exception(exc_type, exc_value, exc_tb)
    with open("assets/logs/db_logs.log", "a") as logf:
        logf.write(f"{dt.datetime.now()} SQLite error:  {(' '.join(er.args))}\n")
        logf.write(f"{dt.datetime.now()} Exception class is:   {er.__class__}\n")
        for item in trcbck:
            logf.write(f"{dt.datetime.now()} {item}")


# active database class
class ActivesDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('assets/database/actives.db')
        self.cursor = self.conn.cursor()

    # connect database
    def database_init(self):
        try:
            print("#+connect_database")
            # create a table (if it doesn't exist)
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS actives 
            (act_id INTEGER PRIMARY KEY AUTOINCREMENT,
            active_name TEXT)''')
            print("#-connect_database")
            self.conn.commit()
        except sqlite3.Error as er:
            log_err(er)

    # create an active
    def create_actives(self, act_id, name):
        try:
            print("#+create_actives")
            self.cursor.execute("INSERT INTO actives(act_id, active_name) VALUES (?,?)", (act_id, name))
            self.conn.commit()
            print("#-create_actives")
        except sqlite3.Error as er:
            log_err(er)
            if str(er.__class__) == "<class 'sqlite3.IntegrityError'>":
                print("Id already exists in database!")

    # read all actives
    def read_actives(self):
        try:
            print("#+read_actives")
            self.cursor.execute("SELECT * FROM actives")
            actives = self.cursor.fetchall()
            print(actives)
            print("#-read_actives")
        except sqlite3.Error as er:
            log_err(er)

    # update actives
    def update_actives(self, act_id, new_name):
        try:
            print("#+update_actives")
            self.cursor.execute("UPDATE actives SET active_name = ? WHERE act_id = ?", (new_name, act_id))
            self.conn.commit()
            print("#-update_actives")
        except sqlite3.Error as er:
            log_err(er)

    # delete actives
    def delete_actives(self, act_id):
        try:
            print("#+delete_actives")
            act_id = int(act_id)
            self.cursor.execute("DELETE FROM actives WHERE act_id = ?", (act_id,))
            self.conn.commit()
            print("#-delete_actives")
        except sqlite3.Error as er:
            log_err(er)
