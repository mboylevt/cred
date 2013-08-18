__author__ = 'matt'

from database.Student import Student
from lib import DBConnect

def add_student(fname,lname,address,city,state):
    '''
    Function to add a student to the database
    '''
    session = DBConnect.connect()

    session.add(Student( first_name=fname,last_name=lname,address=address,city=city,state=state))
    session.commit()

def list_students():
    session = DBConnect.connect()
    for instance in session.query(Student).order_by(Student.id):
        print instance.first_name, instance.last_name
    session.close()

def remove_student(id):
    '''
    TODO: implement
    '''
    #to_remove =
    #d = addresses_table.delete(addresses_table.c.retired == 1)