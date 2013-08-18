__author__ = 'matt'
from datetime import date
import csv
from lib import StudentLib, RecordTypeLib, ClassLib, RecordLib, DBConnect

session = DBConnect.connect()
#RecordLib.add_record(session, 1000,1,2,date.today(),1,0)
#RecordLib.list_records_per_student(session, 1000)
#ClassLib.add_class(session, "Social Studies", 5)
#ClassLib.list_classes(session)
#ClassLib.remove_class_by_id(session,1)
#StudentLib.add_student(session,'Kevin','Boyle','16 Scudder Ct','Pennington','New Jersey')
#StudentLib.list_students(session)
#StudentLib.remove_student_by_id(session,'1002')
#session.commit()

def split_string_into_chunks(s, l):
    return [s[i:i+l] for i in range(0, len(s), l)]

def parse_csv(csv_file):
    # Parse some csv bullshit
    with open(csv_file,'rb') as csvfile:
        cred_reader = csv.reader(csvfile, delimiter=',')
        #data = [row for row in cred_reader]
        #print data

        cred_reader.next() # drop subject header
        mon = (cred_reader.next()[1:], cred_reader.next()[1:])
        tue = (cred_reader.next()[1:], cred_reader.next()[1:])
        wed = (cred_reader.next()[1:], cred_reader.next()[1:])
        thurs = (cred_reader.next()[1:], cred_reader.next()[1:])
        fri = (cred_reader.next()[1:], cred_reader.next()[1:])

    return_list = []
    return_list.append(mon)
    return_list.append(tue)
    return_list.append(wed)
    return_list.append(thurs)
    return_list.append(fri)
    return return_list

def create_records(session, week, student_id):

    types = RecordTypeLib.get_record_types(session)
    classes = ClassLib.get_classes(session)

    dow = 1
    for day in week:
        print "DOW\tClassID\tCRED\tScore"
        for entry in day:
            class_id = 1
            for chunk in split_string_into_chunks(entry,4):
                cred_id = 1
                for column in chunk:
                    if column != '':
                        record_type = [x for x in types if x.id == cred_id][0]
                        class_obj = [x for x in classes if x.class_id == class_id][0]
                        print str(dow) + '\t' + class_obj.name + '\t' + record_type.letter  +'\t' + column
                        RecordLib.add_record(session,student_id,record_type.id,class_obj.class_id,date.today(),dow,column)
                    cred_id = cred_id + 1
                    if cred_id > 4:
                        cred_id = 1
                class_id = class_id + 1
        dow = dow + 1

week = parse_csv('D:\\Downloads\\cred.csv')
create_records(session, week, 1000)



