#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa"""

import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm from sessionmaker, relationship

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for result in session.query(State).order_by(cities.id):
        for result_city in result.cities:
            print(result_city.id, result_city.name, sep=": ", end="")
            print(" -> " + result.name)
