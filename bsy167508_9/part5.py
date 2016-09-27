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
sql="select s.name, c.course_name, g.grade from grades as g join student as s join course as c on c.course_id=g.course_id and s.stu_id=g.stu_id and s.gender=2 having g.grade=max(g.grade)"
cur.execute(sql)
result = cur.fetchall()
for r in result:
    print "%s %s %s" % r
        
        