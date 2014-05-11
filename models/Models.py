__author__ = 'matt'
from sqlalchemy import Column, Integer, Date, ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Student(base):
    """
    Cred Student table.
    This object maps to the Student table
    """
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    date_created = Column(TIMESTAMP)
    date_updated = Column(TIMESTAMP)

    def __repr__(self):
        return "<Student('%s','%s','%s')>" % (self.id, self.last_name, self.first_name)


class Record(base):
    """
    Cred Record table.
    This object maps to the record table, which contains the meaty data we care about.
    """
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    record_type_id = Column(Integer, ForeignKey('record_type.id'))
    class_id = Column(Integer, ForeignKey('class.id'))
    date_of_record = Column(Date)
    day_of_week = Column(Integer)
    score = Column(Integer)

    def __repr__(self):
        return "<Record('%s','%s','%s','%s','%s')>" %\
               (self.id, self.student_id, self.record_type_id, self.class_id, self.score)


class RecordType(base):
    """
    Cred RecordType table.
    This maps a RecordTypeId entry to a letter
    """
    __tablename__ = 'record_type'
    id = Column(Integer, primary_key=True)
    letter = Column(String)

    def __repr__(self):
        return "<('%s','%s')>" % (self.id, self.letter)


class Class(base):
    """
    Cred Class table.
    This defines information about a class
    """
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    times_per_week = Column(Integer)
    class_id = Column(Integer)

    def __repr__(self):
        return "<('%s','%s','%s')>" % (self.id, self.name, self.times_per_week)