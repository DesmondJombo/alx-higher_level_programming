#!/usr/bin/python3
'''3-my_safe_filter_states module'''
import MySQLdb
import sys

if __name__ == "__main__":
    ''' takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa where name matches
    the argument.'''
    connection = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )

    cur = connection.cursor()

    name_matches = sys.argv[4]

    query = (
        "SELECT * FROM states WHERE name "
        "LIKE %s ORDER BY id ASC"
    )

    cur.execute(query, (name_matches,))
    state_col = cur.fetchall()

    for row in state_col:
        print("{}".format(row))

    cur.close()
    connection.close()
