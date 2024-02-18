#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py that prints all City
 objects from the database hbtn_0e_14_usa:"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    s = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(s)

    c = Session(s)
    for i, j in session.query(State, City).filter(City.state_id == State.id).order_by(City.id).all():
            print("{}: ({}) {}".format(i.name, j.id, j.name))
    c.close()
