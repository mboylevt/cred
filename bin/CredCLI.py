__author__ = 'matt'

from database.Student import Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://matt:testpassword@localhost')
engine.execute('use cred')

Session = sessionmaker(bind=engine)
session = Session()

#result = engine.execute('show tables')
#for row in result:
#    print row['Tables_in_cred']

kathleen_student = Student( first_name='Kathleen',
                            last_name='Boyle',
                            address='2532 30th Drive 4C',
                            city='Astoria',
                            state='New York')
session.add(kathleen_student)
session.commit()

print kathleen_student.id

result = engine.execute('show tables')
for row in result:
    print row['Tables_in_cred']
