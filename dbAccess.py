
import sqlite3

class DB_Access:
    def __init__(self, db_file_location:str) -> None:
        self.connection = sqlite3.connect(db_file_location, check_same_thread=False)
        self.mycursor = self.connection.cursor()

    def insert_new_registration_data(self, names, passwords, phones, emails, addresss) -> bool:
        sqlite_insert_query = f"INSERT INTO registration (full_name, email, password, phone, address) VALUES (?, ?, ?, ?, ?)"
        self.mycursor.execute(sqlite_insert_query, (names, emails, passwords, int(phones), addresss))
        self.connection.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False

    def check_login_data(self, emails, passwords) -> bool:
        self.mycursor.execute(
            "SELECT * FROM registration WHERE email = (?) AND password = (?)",
            (emails, passwords))
        result = self.mycursor.fetchall()
        if len(result) > 0:
            return True
        else:
            return False
