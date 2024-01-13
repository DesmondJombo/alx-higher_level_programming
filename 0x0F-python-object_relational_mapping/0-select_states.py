#!/usr/bin/python3
'''The 0-select_states module'''
import MySQLdb
import sys

if __name__ == "__main__":
    ''' lists all states from the database hbtn_0e_0_usa'''
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    state_col = cur.fetchall()

    for row in state_col:
        print("{}".format(row))

    cur.close()
    db.close()
