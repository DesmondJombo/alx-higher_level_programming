#!/usr/bin/python3
"""7-model_state_fetch_all module"""
from model_state import Base, State
from sqlalchemy import create_engine, select
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, passwd, db), pool_pre_ping=True)

    conn = engine.connect()

    Base.metadata.reflect(engine)
    states = Base.metadata.tables['states']

    query = select(states).order_by(states.c.id.asc())

    output = conn.execute(query)

    result = output.fetchone()

    if not result:
        print("Nothing\n")
    else:
        print("{}: {}".format(result.id, result.name))

    Base.metadata.create_all(engine)
