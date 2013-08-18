__author__ = 'matt'

from lib import StudentLib, RecordTypeLib, DBConnect

session = DBConnect.connect()
RecordTypeLib.list_record_types(session)

#StudentLib.add_student(session,'Kevin','Boyle','16 Scudder Ct','Pennington','New Jersey')
#StudentLib.list_students(session)
#StudentLib.remove_student_by_id(session,'1002')
#session.commit()

