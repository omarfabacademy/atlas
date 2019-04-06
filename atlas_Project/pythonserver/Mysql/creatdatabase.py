
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","omar","firstblog" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "Create TABLE S (id INT AUTO_INCREMENT PRIMARY KEY, Sn VARCHAR(255), Vl INT NULL ,y INT NULL,mm INT NULL,d INT NULL,h INT NULL,m INT NULL,s INT NULL,ms INT NULL)"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print "omar"
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
