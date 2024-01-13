#!/usr/bin/python3
'''4-cities_by_state module'''
import MySQLdb
import sys


if __name__ == "__main__":
    ''' lists all cities from the database hbtn_0e_4_usa'''
    connection = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )

    cur = connection.cursor()

    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY id ASC"
    )

    cur.execute(query)

    cities = cur.fetchall()

    for city in cities:
        print("{}".format(city))

    cur.close()
    connection.close()
