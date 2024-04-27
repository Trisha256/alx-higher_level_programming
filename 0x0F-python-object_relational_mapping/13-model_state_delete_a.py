#!/usr/bin/python
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

    # Query the State objects with names containing the letter "a"
    states_to_delete = session.query(State).filter
    (State.name.like("%a%")).all()

    # Delete the matching states
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()