__author__ = 'matt'

from sqlalchemy import Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base as Base


class Record(Base()):
    '''
    Cred Record table.  This object maps to the record table, which contains the meaty data we care about.
    '''
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    record_type_id = Column(Integer)
    class_id = Column(Integer)
    date_of_record = Column(Date)
    day_of_week = Column(Integer)
    score = Column(Integer)

    def __repr__(self):
        return "<Record('%s','%s','%s','%s','%s')>" % \
               (self.id, self.student_id, self.record_type_id, self.class_id, self.score)