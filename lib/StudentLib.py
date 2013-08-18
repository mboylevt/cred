__author__ = 'matt'

from database.Tables import Student

def add_student(session,fname,lname,address,city,state):
    '''
    Function to add a student to the database
    '''
    student = Student( first_name=fname,last_name=lname,address=address,city=city,state=state)
    session.add(student)
    session.commit()

def list_students(session):

    for instance in session.query(Student).order_by(Student.id):
        print instance.first_name, instance.last_name

def remove_student_by_id(session,id):
    '''
    TODO: implement
    '''
    to_remove = session.query(Student).filter(Student.id==int(id))[0]
    print to_remove
    session.delete(to_remove)