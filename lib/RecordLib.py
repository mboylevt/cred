__author__ = 'matt'

from database.Record import Record

def add_record(session, student_id, record_type_id, class_id, date, dow, score):
    '''
    Function to add a record to the database
    '''
    session.add(Record(student_id=student_id, record_type_id=record_type_id,
        class_id=class_id, date_of_record=date, day_of_week=dow, score=score))
    session.commit()

def list_records_per_student(session, student_id):
    '''
    Function to list all records belonging to a student
    Not particularly useful in data analysis, mostly for debugging's sake
    '''
    for instance in session.query(Record).order_by(Record.id).filter(Record.student_id == student_id):
        print instance.id, instance.student_id, instance.score