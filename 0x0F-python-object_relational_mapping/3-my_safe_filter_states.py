#!/usr/bin/python3

"""
 lists all states from the database hbtn_0e_0_usa that has the name
 Safe against injection
"""


if __name__ == '__main__':

    import sys
    import MySQLdb

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user_name, passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name=%s
                   ORDER BY states.id ASC; """, (name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
