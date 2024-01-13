#!/usr/bin/python3
'''The 1-filter_states module'''
import MySQLdb
import sys

if __name__ == "__main__":
    '''lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa'''
    connection = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )

    cur = connection.cursor()

    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY'{}' "
            "ORDER BY id ASC".format('N%')
            )
    state_col = cur.fetchall()

    for row in state_col:
        print("{}".format(row))

    cur.close()
    connection.close()
