from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=True)
    username = Column(String(50), unique=True, nullable=False)
    hpwd = Column(String(255), nullable=False)


engine = create_engine("sqlite:///users.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def get_user(Session, username: str) -> User:
    with Session.begin() as session:
        try:
            return session.query(User).filter(User.username==username).first()
        except NoResultFound:
            return None



if __name__ == '__main__':
    # Create the database and add a new user 
    from util.passwords import hash

    # id is automatically generated
    new_user = User(
        username = "user1", 
        hpwd=hash('P@ss12345'))

    with Session.begin() as session:       
            session.add(new_user)


