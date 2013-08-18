-- student table 
CREATE TABLE IF NOT EXISTS student
(
id int NOT NULL AUTO_INCREMENT,
last_name varchar(255) NOT NULL,
first_name varchar(255),
address varchar(255),
city varchar(255),
state varchar(2),
date_created TIMESTAMP DEFAULT now(),
date_updated TIMESTAMP DEFAULT now(),
PRIMARY KEY (id)
);

ALTER TABLE student AUTO_INCREMENT=1000;

INSERT INTO student (last_name, first_name, address, city, state)
VALUES ('Boyle','Matt','2532 30th Drive 4C','Astoria','NY');

-- Record types -- specific to C.R.E.D. program
CREATE TABLE IF NOT EXISTS record_type
(
id int NOT NULL AUTO_INCREMENT,
letter varchar(2) NOT NULL,
PRIMARY KEY (id)
);

INSERT INTO record_type (letter)
VALUES ('C'),('R'),('E'),('D');

-- class
CREATE TABLE IF NOT EXISTS class
(
id int NOT NULL AUTO_INCREMENT,
name varchar(255) NOT NULL,
times_per_week int NOT NULL,
PRIMARY KEY (id)
);

ALTER TABLE student AUTO_INCREMENT=1000;

-- record -- table representing a record entity
CREATE TABLE IF NOT EXISTS record
(
id int NOT NULL AUTO_INCREMENT,
student_id int NOT NULL,
record_type_id int NOT NULL,
class_id int NOT NULL,
date_of_record DATE NOT NULL,
day_of_week int NOT NULL,
score bit NOT NULL,
date_created TIMESTAMP DEFAULT now(),
date_updated TIMESTAMP DEFAULT now(),
PRIMARY KEY (id)
);

ALTER TABLE record AUTO_INCREMENT=1000;

