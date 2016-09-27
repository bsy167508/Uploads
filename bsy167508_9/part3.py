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
print "\nA scorers"
#Print names of students who scored atleast an A in any subjects taught by Subrat Kar
sql = "select distinct s.name from student as s join grades as g join enroll as e join course as c on e.course_id=c.course_id and s.stu_id=g.stu_id and s.stu_id=e.stu_id where c.instructor='Subrat Kar' and g.grade=10"
cur.execute(sql)
result = cur.fetchall()

for r in result:
    print r[0]