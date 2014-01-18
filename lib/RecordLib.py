__author__ = 'matt'

from models.Models import Record

def add_record(session, student_id, record_type_id, class_id, date, dow, score):
    '''
    Function to add a record to the models
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

def calculate_percentage(session, student_id, class_id, record_type):
    '''
    Calculate a student's percentage based on a particular record type
    '''
    total_points = 0
    points_earned = 0
    for instance in session.query(Record).filter(Record.student_id == student_id, Record.record_type_id == record_type, Record.class_id == class_id):
        total_points = total_points + 1
        if instance.score == 1:
            points_earned = points_earned + 1

    print "For record_type {type}, student {student} earned {poss}/{total}".format(type=record_type,student=student_id,poss=points_earned,total=total_points)