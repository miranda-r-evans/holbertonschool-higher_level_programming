#!/usr/bin/python3
"""
changes a state name to 'New Mexico' using SQLAlchemy
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
        session.query(State).filter(State.id == 2).first().name = 'New Mexico'
        session.commit()
