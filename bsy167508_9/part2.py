import MySQLdb

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
    
 #Find students enrolled in both CTheory and TMS       
 
sql = "select student.name from student, course, enroll where student.stu_id=enroll.stu_id and enroll.course_id=course.course_id and course.course_name='Telecom Management Systems' and student.stu_id in (select student.stu_id from student, course, enroll where student.stu_id=enroll.stu_id and enroll.course_id=course.course_id and course.course_name='Coding Theory')"
cur.execute(sql)
result = cur.fetchall()
print "Subject takers"
for r in result:
    print r[0]