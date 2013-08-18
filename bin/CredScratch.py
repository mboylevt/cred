__author__ = 'matt'
from datetime import date
from lib import StudentLib, RecordTypeLib, ClassLib, RecordLib, DBConnect

session = DBConnect.connect()
RecordLib.add_record(session, 1000,1,2,date.today(),1,0)
#ClassLib.add_class(session, "Social Studies", 5)
#ClassLib.list_classes(session)
#ClassLib.remove_class_by_id(session,1)
#StudentLib.add_student(session,'Kevin','Boyle','16 Scudder Ct','Pennington','New Jersey')
#StudentLib.list_students(session)
#StudentLib.remove_student_by_id(session,'1002')
#session.commit()

