__author__ = 'matt'

from database.Tables import RecordType


def list_record_types(session):
    for instance in session.query(RecordType).order_by(RecordType.id):
        print instance.id, instance.letter

def get_record_types(session):
    return session.query(RecordType).order_by(RecordType.id).all()