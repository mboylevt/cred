__author__ = 'matt'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base as Base

class Class(Base()):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    times_per_week = Column(Integer)

    def __repr__(self):
        return "<('%s','%s','%s')>" % (self.id, self.name, self.times_per_week)