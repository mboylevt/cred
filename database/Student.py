__author__ = 'matt'

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from database import Base

class Student(Base.base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    date_created = Column(TIMESTAMP)
    date_updated = Column(TIMESTAMP)
    record = relationship('Record', order_by=('Record.id'), backref='student')

    def __repr__(self):
        return "<Student('%s','%s','%s')>" % (self.id, self.last_name, self.first_name)