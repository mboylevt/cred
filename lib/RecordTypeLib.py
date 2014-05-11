__author__ = 'matt'

from models.Models import RecordType


def list_record_types(session):
    for instance in session.query(RecordType).order_by(RecordType.id):
        print instance.id, instance.letter


def get_record_types(session):
    """
    @rtype: [RecordType]
    """
    return session.query(RecordType).order_by(RecordType.id).all()