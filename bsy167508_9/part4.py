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

#Avg score for each course
print "\nAverage marks course wise\n"
sql="select c.course_name, round(avg(g.grade),2) from grades as g join course as c on c.course_id=g.course_id group by c.course_id"
cur.execute(sql)
result = cur.fetchall()
for r in result:
    print "%s %s" % r