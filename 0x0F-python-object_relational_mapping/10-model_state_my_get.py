#!/usr/bin/python3
"""
prints a given state object using SQLAlchemy
"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)
from sys import argv


if __name__ == "__main__":
        string = 'mysql+mysqldb://{}:{}@localhost/{}'
        engine = create_engine(string.format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter(State.name == argv[4]).first()
        if state is None:
                print('Not found')
        else:
                print(state.id)
