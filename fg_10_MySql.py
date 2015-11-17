__author__ = 'Sawl_Stone'

import mysql.connector

def main():
    cnx = mysql.connector.connect(
        user='root',
        password='12345',
        host='127.0.0.1',
        database='pythondb')

    cursor = cnx.cursor()
    sqlQuerty = "INSERT INTO CLIENTS (name, surname) VALUES('aaa', 'bbb')"

    cursor.execute(sqlQuerty)
    cnx.commit()
    cnx.close()

main()