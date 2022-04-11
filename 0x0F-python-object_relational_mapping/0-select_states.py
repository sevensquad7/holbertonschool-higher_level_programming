#!/usr/bin/python3
"""script that lists all states from the database"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db_connection = MySQLdb.connect(host='localhost',
                                    port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db_connection=sys.argv[3])
    cur = db_connection.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_connection.close()
