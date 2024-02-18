#!/usr/bin/python3
"""script that deletes all State objects with a name containing
 the letter a from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    s = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
	sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(s)

    c = Session(s)
    for i in c.query(i).filter(State.name.like('%a%')):
        c.delete(i)
    c.commit()
    c.close()
