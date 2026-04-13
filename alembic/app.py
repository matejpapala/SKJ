from model import User, Post
from database import engine
from sqlalchemy.orm import Session
from sqlalchemy import select


# with Session(engine) as session:
#     u1 = User(name = "Adam ", email = "adam@vsb.cz")
#     u2 = User(name = "Eva ", email = "eva@vsb.cz")
#     session.add_all([u1, u2])
#     session.commit()


with Session(engine) as session:
    stmt = select(User)

    result = session.execute(stmt).scalars().all()
    for user in result:
        print(user)