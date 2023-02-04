# Standard imports
from typing import Dict

# SA imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# Custom imports
from database.models import Base, User


engine = create_engine("sqlite:///users.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def get_user(username: str) -> Dict:
    with Session.begin() as session:
        try:
            user = session.query(User).filter(User.username==username).first()
            return {k:v for k,v in user.__dict__.items() if k != 'id'}
        except NoResultFound:
            return None


if __name__ == '__main__':
    # Create the database and add a new user 

    # add the backend folder to the path
    import os, sys
    current_directory = os.getcwd()
    if current_directory.endswith('database'):
        os.chdir('..')
        current_directory = os.getcwd()
    sys.path.append(current_directory)

    from util.passwords import hash_password
    
    # id is automatically generated
    new_user = User(
        username = "user1", 
        hpwd = hash_password('P@ss12345'))

    with Session.begin() as session:       
            session.add(new_user)
