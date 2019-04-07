import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="omar",
  database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))") 
#For Creating Table 

#mycursor.execute("ALTER TABLE customers ADD COLUMN omar INT  ") 
#For Adding Column 


#this is for inserting one value
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
'''



#Inserting Multiple Values 

'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 

'''



#To get the ID of an Last Inserted ROW

'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid) 

'''



#To Show all Data entered 

'''
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
  
'''


#to fetch first one line 
'''
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult) 
'''

#To Search In data 
'''
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''

#To search with word 

'''
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 

'''

#Using %s is to prevent SQL Injection 

'''
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 
'''

#For Sorting

'''
sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
'''


#For Sorting Descending

'''
sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 
'''

#For Deleting based on Parameters

'''
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
'''

#For Preventing SQL Injection using %s
'''
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted") 
'''

#For Deleting a Whole Table

'''
sql = "DROP TABLE customers"

mycursor.execute(sql) 
'''


#For Deleting a Table if still exists

'''
sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql) 
'''

#For Updating Specific data 
'''
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Valley 345", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 
'''


#to changle coloumn name 
#mycursor.execute("ALTER TABLE sensors Change address value int ")
