#!/usr/bin/python3
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

    # Query the first State object
    state = session.query(State).order_by(State.id).first()

    # Display the result
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
