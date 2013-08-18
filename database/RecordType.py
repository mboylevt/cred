__author__ = 'matt'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base as Base

class RecordType(Base()):
    __tablename__ = 'record_type'
    id = Column(Integer, primary_key=True)
    letter = Column(String)

    def __repr__(self):
        return "<('%s','%s')>" % (self.id, self.letter)