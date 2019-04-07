# Echo server program
import socket
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="omar",
  database="Fishfarms"

)

mycursor = mydb.cursor()


HOST = '10.42.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50008             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
s1=0
s2=0
s3=0
s4=0
s11=0
s22=0
s33=0
s44=0
while 1:
	while 1:
		data = conn.recv(1024) 
		#print "before"
		#print data
		#print len(data)
		data =data.replace("\r","")
		data =data.replace('\r','')
		#print "after"
		#print data
		#print len(data)
		#print "-----------------------------------"
		if data[1:] != "":
			if data[0] == 'a' :
				#print "Sensor 1 = " + data [1:]
				o=data[1:]
				o=o.strip()
				if o.count(".",0,len(o)) <=1 :
					print "omar",o,"omar"
			
					if 'E' in o :
						s5="ER"
					elif 'O' in o : 
						s5="ER"
					elif ' ' in o : 
						s5="ER"
							
					else :
						try :
							if o < 60 & o>0 : 
								if abs(s1-s11) < 5 | s11==0 :
									s1=float(o)
									s11=s1
								else :
									s1=s11
								
								
						except :
							s5="error"
					if s1 > 1000 : 
							s5="ER"
					
					#print "s1 = " , s1
				
				print "==========================="
				print "The First Sensor -Temperature- Equal = ",s1
				print "==========================="
				omar = 0 
				

			if data[0] == 'b' :
				#print "Sensor 2 = " + data [1:]
				o=data[1:]
				o=o.strip()
				if o.count(".",0,len(o)) <=1 :
					
					if 'E' in o :
						s5="ER"
					elif 'O' in o : 
						s5="ER"
					elif ' ' in o : 
						s5="ER"
							
					else :
						try :
							if o < 60 & o>0 : 
								if abs(s2-s22) < 5 | s22==0 :
									s2=float(o)
									s22=s2
								else :
									s2=s22
						except :
							s5="error"
						if s2 > 1000 : 
							s5="ER"
					
						#print "s2 = " , s2
				
				print "==========================="
				print "The Second Sensor -Oxygen Level- Equal = ",s2
				print "==========================="

			if data[0] == 'c' :
				#print "Sensor 3 = " + data [1:]
				o=data[1:]
				o=o.strip()
				if o.count(".",0,len(o)) <=1 :
					if 'E' in o :
						s5="ER"
					elif 'O' in o : 
						s5="ER"
					elif ' ' in o : 
						s5="ER"
					
					else :
						try :
							
							if o < 60 & o>0 : 
								if abs(s3-s33) < 5 | s33==0 :
									s3=float(o)
									s33=s3
								else :
									s3=s33
						except :
							s5="error"
								
						if s3 > 1000 : 
							s5="ER"
					
					#print "s3 = " , s3
				
				
				print "==========================="
				print "The Third Sensor -PH- Equal = ",s3
				print "==========================="

			if data[0] == 'd' :
				#print "Sensor 4 = " + data [1:]
				o=data[1:]
				o=o.strip()
				if o.count(".",0,len(o)) <=1 :
					if 'E' in o :
						s5="ER"
					elif 'O' in o : 
						s5="ER"
					elif ' ' in o : 
						s5="ER"
					
					else :
						try : 
							
							if o < 60 & o>0 : 
								if abs(s4-s44) == 5 | s44==0 :
									s4=float(o)
									s44=s4
								else :
									s4=s44
							print "Done TRY"
						except : 
							s5="Error"
						if s4 > 1000 : 
								s5="ER"
					#print "s4 = " , s4
				
				print "==========================="
				print "The Fourth Sensor -ORP- Equal = ",s4
				print "==========================="
				omar = 1 
			if omar == 1 : 
				sql = "INSERT INTO sensors (TEMP,DO,PH,ORP) VALUES (%s,%s,%s,%s)"
				val = [
				  (s1,s2,s3,s4)
				]

				mycursor.executemany(sql, val)

				mydb.commit()

				print(mycursor.rowcount, "was inserted.") 
			
		



conn.close()
