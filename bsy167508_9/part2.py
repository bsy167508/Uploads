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
 
sql = "select distinct s.name from student as s join course as c join enroll as e on e.course_id=c.course_id and e.stu_id=s.stu_id where course_name='Coding Theory' or course_name='Telecom Management Systems'"
cur.execute(sql)
result = cur.fetchall()
print "Subject takers"
for r in result:
    print r[0]