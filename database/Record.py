__author__ = 'matt'

from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base as Base

class Record(Base()):
    '''
    Cred Record table.  This object maps to the record table, which contains the meaty data we care about.
    '''
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    record_type_id = Column(Integer, ForeignKey('record_type.id'))
    class_id = Column(Integer, ForeignKey('class.id'))
    date_of_record = Column(Date)
    day_of_week = Column(Integer)
    score = Column(Integer)

    student = relationship("Student", backref=backref('record', order_by=id))

    def __repr__(self):
        return "<Record('%s','%s','%s','%s','%s')>" % \
               (self.id, self.student_id, self.record_type_id, self.class_id, self.score)