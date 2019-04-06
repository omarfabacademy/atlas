
#!/usr/bin/python

import MySQLdb

import datetime

now = datetime.datetime.now()



# Open database connection
db = MySQLdb.connect("localhost","root","omar","firstblog" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


y = int(now.year)
mm = int(now.month)
d =  int(now.day)
h = int(now.hour)
m =  int(now.minute)
s = int(now.second)
ms = int(now.microsecond)

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO S (Sn, Vl,y,mm,d,h,m,s,ms) VALUES ("{}", {} , {}, {}, {}, {}, {}, {}, {})""".format("Peter",1, y,mm,d,h,m,s,ms)
  
print sql
#print val
  

try:
   # Execute the SQL command
   	print "123"

	cursor.execute(sql)
	print(cursor.rowcount, "record inserted.")

   	print "123"

    # Commit your changes in the database
	db.commit()
	print "Hello"
except:
	print "omar"
   # Rollback in case there is any error
	db.rollback()
# disconnect from server
db.close()
