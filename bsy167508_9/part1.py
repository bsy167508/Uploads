import MySQLdb, random

# Open database connection
db = MySQLdb.connect("localhost","root","12345678","mydb" )
db.autocommit(True)
# prepare a cursor object using cursor() method
cur = db.cursor() 
# see if connection was made successfully.
try:
    cur.execute("SELECT VERSION()")
    results = cur.fetchone()
    # Check if anything at all is returned
    if results:
        print "Connected to database."               
except MySQLdb.Error as e:
    print "ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1])
 
 
 # Create tables as per requirement   
sql="DROP TABLE IF EXISTS student"
cur.execute(sql)

sql = """create table student(
            stu_id int NOT NULL auto_increment,
            name varchar(30),
            gender ENUM('male', 'female'),
            primary key(stu_id) )"""
            
cur.execute(sql)

sql="DROP TABLE IF EXISTS course"
cur.execute(sql)
sql = """create table course(
            course_id int NOT NULL auto_increment,
            course_name varchar(30),
            instructor varchar(30),
            primary key(course_id) )"""
            
cur.execute(sql)

sql="DROP TABLE IF EXISTS enroll"
cur.execute(sql)
sql = """create table enroll(
            stu_id int NOT NULL,
            course_id int NOT NULL)"""
            
cur.execute(sql)

sql="DROP TABLE IF EXISTS grades"
cur.execute(sql)
sql = """create table grades(
            id int NOT NULL auto_increment,
            stu_id int NOT NULL,
            course_id int NOT NULL,
            grade int,
            primary key(id) )"""
            
cur.execute(sql)

#Populate the tables with suitable data.
cur.executemany("insert into student(name, gender) values(%s, %s)", [('abhishek', 1), ('karan', 1), ('priyanka', 2), ('monika', 2), ('ram', 1), ('shyam', 1), ('seeta', 2), ('geeta', 2)])
cur.executemany("insert into course(course_name, instructor) values(%s, %s)", [('Signal Theory', 'Mahim Sagar'), ('Telecom Software Lab', 'Subrat Kar'), ('Computer Networks', 'Ranjan Bose'), ('Broadband Communication', 'Mahim Sagar'), ('Coding Theory', 'Ranjan Bose'), ('Digital Communication', 'Shankar Prakriya'), ('Telecom Technology', 'Subrat Kar'), ('Telecom Management Systems', 'Shankar Prakriya')])

#enroll students
for i in range(1,9):
    if not i%2==0:
        cur.executemany("insert into enroll(stu_id, course_id) values(%s, %s)", [(i, k) for k in range(1,5)])
    else:
        cur.executemany("insert into enroll(stu_id, course_id) values(%s, %s)", [(i, k) for k in range(5,9)])

#grade the students
lis=[]
for i in xrange(4):
    lis = lis+random.sample([k for k in xrange(3,11)],8)

lis2 = list(enumerate(lis))
for i in xrange(32):
    lis2[i]=tuple(reversed(lis2[i]))

for i in range(1,9):
    if not i%2==0:
        cur.executemany("insert into grades(stu_id, course_id) values(%s, %s)", [(i, k) for k in range(1,5)])
    else:
        cur.executemany("insert into grades(stu_id, course_id) values(%s, %s)", [(i, k) for k in range(5,9)])
cur.executemany("update grades set grade=%s where id=%s+1", lis2)
       



 


