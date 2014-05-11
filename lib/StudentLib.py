__author__ = 'matt'

from models.Models import Student

def add_student(session,fname,lname,address,city,state):
    """
    Function to add a student to the models
    """
    student = Student( first_name=fname,last_name=lname,address=address,city=city,state=state)
    session.add(student)
    session.commit()

def list_students(session):
    for instance in session.query(Student).order_by(Student.id):
        print instance.first_name, instance.last_name

def get_students(session):
    return session.query(Student).order_by(Student.id)

def find_students(session, first_name=None):
    return session.query(Student).filter_by(first_name=first_name).all()

def remove_student_by_id(session,id):
    """
    TODO: implement
    """
    to_remove = session.query(Student).filter(Student.id==int(id))[0]
    print to_remove
    session.delete(to_remove)