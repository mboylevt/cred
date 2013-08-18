__author__ = 'matt'
from datetime import date
import csv
from lib import StudentLib, RecordTypeLib, ClassLib, RecordLib, DBConnect

#session = DBConnect.connect()
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

    return [mon,tue,wed,thurs,fri]

week = parse_csv('D:\\Downloads\\cred.csv')
cred_dict={}
cred_dict[1] = 'c'
cred_dict[2] = 'r'
cred_dict[3] = 'e'
cred_dict[4] = 'd'

dow = 1
for day in week:
    print "DOW\tClassID\tCRED\tScore"
    for entry in day:
        class_id = 1
        for chunk in split_string_into_chunks(entry,4):
            cred_id = 1
            for column in entry:
                if column != '':
                    print str(dow) + '\t' + str(class_id) + '\t' + cred_dict[cred_id]  +'\t' + column
                cred_id = cred_id + 1
                if cred_id > 4:
                    cred_id = 1
            class_id = class_id + 1
    dow = dow + 1
