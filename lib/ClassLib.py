__author__ = 'matt'

from models.Models import Class

def add_class(session,name,times,class_id):
    '''
    Function to add a class to the DB
    '''
    session.add(Class(name=name,times_per_week=times,class_id=class_id))
    session.commit()

def list_classes(session):

    for instance in session.query(Class).order_by(Class.id):
        print instance.name, instance.times_per_week

def get_classes(session):
    return session.query(Class).order_by(Class.id).all()

def remove_class_by_id(session,id):
    '''
    Function to remove a class from the DB
    '''
    to_remove = session.query(Class).filter(Class.id==int(id))[0]
    print to_remove
    session.delete(to_remove)
    session.commit()