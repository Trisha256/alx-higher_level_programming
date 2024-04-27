#!/usr/bin/python3
"""a Python file similar to model_state.py named model_city.py that
contains the class definition of a City
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State


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

    # Query all City objects from the database, sorted by city id
    cities = session.query(City).order_by(City.id).all()

    # Print the cities in the required format
    for city in cities:
        state_name = session.query(State.name).filter
        (State.id == city.state_id).scalar()
        print(f"{state_name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
