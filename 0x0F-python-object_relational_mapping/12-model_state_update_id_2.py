#!/usr/bin/python3
"""
a script that changes the name of a State object from
the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine
    (f"mysql://{username}:{password}@localhost:3306/{database}")

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Change the name of the state to "New Mexico"
    if state:
        state.name = "New Mexico"
        session.commit()
        print(state.id)
    else:
        print("State not found")

    # Close the session
    session.close()
