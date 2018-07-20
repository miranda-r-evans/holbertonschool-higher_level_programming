#!/usr/bin/python3
"""
prints all city objects using SQLAlchemy
"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sys import argv


if __name__ == "__main__":
        string = 'mysql+mysqldb://{}:{}@localhost/{}'
        engine = create_engine(string.format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        my_cities = session.query(State,
                                  City).filter(State.id == City.state_id).all()
        for state, city in my_cities:
                print('{}: {}'.format(state.name, city))
