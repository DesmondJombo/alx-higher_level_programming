#!/usr/bin/python3
'''5-filter_cities'''
import MySQLdb
import sys


if __name__ == "__main__":
    ''' lists all cities from the database hbtn_0e_4_usa'''
    if len(sys.argv) != 5:
        sys.exit(1)

    connection = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )

    cur = connection.cursor()

    state_name = sys.argv[4]

    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON states.id = cities.state_id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cur.execute(query, (state_name,))

    cities = cur.fetchall()

    for i, city in enumerate(cities):
        print("{}".format(city[0]), end="")
        if i < len(cities) - 1:
            print(', ', end="")
    print('\n', end="")

    cur.close()
    connection.close()
