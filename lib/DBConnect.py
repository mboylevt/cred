__author__ = 'matt'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.Config import config

def connect():
    engine = create_engine(config.db_connection_string)
    engine.execute('use cred')

    Session = sessionmaker(bind=engine)
    return Session()