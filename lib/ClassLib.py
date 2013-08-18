__author__ = 'matt'

from database.Class import Class

def add_class(session,name,times):
    '''
    Function to add a class to the DB
    '''
    session.add(Class(name=name,times_per_week=times))
    session.commit()

def list_classes(session):

    for instance in session.query(Class).order_by(Class.id):
        print instance.name, instance.times_per_week

def remove_class_by_id(session,id):
    '''
    Function to remove a class from the DB
    '''
    to_remove = session.query(Class).filter(Class.id==int(id))[0]
    print to_remove
    session.delete(to_remove)
    session.commit()