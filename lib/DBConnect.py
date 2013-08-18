__author__ = 'matt'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect():
    engine = create_engine('mysql://matt:testpassword@localhost')
    engine.execute('use cred')

    Session = sessionmaker(bind=engine)
    return Session()