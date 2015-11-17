__author__ = 'Sawl_Stone'

import mysql.connector

def main():
    cnx = mysql.connector.connect(
        user='root',
        password='12345',
        host='127.0.0.1',
        database='pythondb')

    cursor = cnx.cursor()
    sqlQuerty = "select * from clients"

    cursor.execute(sqlQuerty)

    s = ""
    for row in cursor:
        s = str(row[0]) + " " + row[1] + " " + row[2] + "\n"
    print(s)
    cnx.close()

main()