#!/usr/bin/python3
"""script that prints the State object with the name passed as
 argument from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    s = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(s)

    c = Session(s)
    t = c.query(State).filter(State.name == sys.argv[4]).first()
    if t:
        print("{}".format(t.id))
    else:
        print("Not found")
    c.close()
