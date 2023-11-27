import pandas as pd
import mysql.connector
from mysql.connector import MySQLConnection, Error


class DB_Access:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="appdb"
        )
        self.mycursor = self.mydb.cursor()

    def insert_new_registration_data(self,  names, passwords, phones, emails, addresss) -> bool:
        self.mycursor.execute(
            "INSERT INTO registration (name, password, phone, email, address) VALUES (%s, %s, %s, %s, %s)",
            (names, passwords, phones, emails, addresss))
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False


    def check_login_data(self, emails, passwords) -> bool:
        self.mycursor.execute(
            "SELECT * FROM registration WHERE email = %s AND password = %s",
            (emails, passwords))
        result = self.mycursor.fetchall()
        if len(result) > 0:
            return True
        else:
            return False

