#!/usr/bin/python3
"""This module that adds a new state to the MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Creates the SQLAlchemy engine using the provided MySQL credentials.
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creates the session factory.
    Session = sessionmaker(bind=engine)

    # Creates the session object.
    session = Session()

    # Creates the new State object for Louisiana.
    louisiana = State(name="Louisiana")
    # Adding the new state to the session.
    session.add(louisiana)
    # Commits the session to persist the changes.
    session.commit()
    # Prints the ID of the newly added state.
    print(louisiana.id)
