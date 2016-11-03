import MySQLdb
from _mysql import NULL

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


#girl student who topped in the course
print "Check if there is any girl topper in any subject:"
for course_id in xrange(1,9):
#     print "%d %d" % (1, 1)
    sql="select s.name, g.grade, c.course_name from student as s join enroll as e join grades as g join course as c where e.course_id=g.course_id and s.stu_id=e.stu_id and e.course_id=c.course_id and e.course_id= %d  and g.grade in (select max(g.grade) from grades as g join course as c where c.course_id=g.course_id and c.course_id= %d ) and s.gender=2" % (course_id, course_id)
    cur.execute(sql)
    result = cur.fetchall()
    for r in result:
        print "%s %s %s" % r
        
        