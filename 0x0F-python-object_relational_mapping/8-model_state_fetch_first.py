#!/usr/bin/python3
'''First state'''


if __name__ == "__main__":
    """ Start link class to table in database"""
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine, select

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    query = select(State).order_by(State.id.asc())
    with engine.connect() as connection:
        # Use order_by with first directly
        state = connection.execute(query).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("No states found.")
    engine.dispose()
