#!/usr/bin/python3
"""script that lists all states from the database"""

import MySQLdb
import sys


def mysqlconnect():
    try:
        db_connection = MySQLdb.connect(host='localhost',
                                        port=3306,
                                        user=sys.argv[1],
                                        passwd=sys.argv[2],
                                        db_connection=sys.argv[3])
    except:
        print("Error while connecting to MySQL")
        return 0
    print("Connected")
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_connection.close()


mysqlconnect()
