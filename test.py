import sqlite3



if __name__ == '__main__':


    connection = sqlite3.connect('app_db.db')
    cur = connection.cursor()
    cur.execute('SELECT full_name from REGISTRATION')
    print(cur.fetchall())
    connection.close()
    D =  {'name': 'John', 'age': 25, 'city': 'New York'}

