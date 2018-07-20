#!/usr/bin/env python3
"""
state class
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+mysqldb://...', pool_recycle=3600)
Base = declarative_base()

class State(Base):
        """
        class representing a state
        """
        __tablename__ = states
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
