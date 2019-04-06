# Echo server program
import socket

HOST = '10.32.14.113'                 # Symbolic name meaning all available interfaces
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
						s1="ER"
					elif 'O' in o : 
						s1="ER"
					elif ' ' in o : 
						s1="ER"
							
					else :
						try : 
							s1=float(o)
						except :
							s1="error"
						
					#print "s1 = " , s1
				
				print "==========================="
				print "The First Sensor -Temperature- Equal = ",s1
				print "==========================="
				

			if data[0] == 'b' :
				#print "Sensor 2 = " + data [1:]
				o=data[1:]
				o=o.strip()
				if o.count(".",0,len(o)) <=1 :
					
					if 'E' in o :
						s2="ER"
					elif 'O' in o : 
						s2="ER"
					elif ' ' in o : 
						s2="ER"
							
					else :
						try : 
							s2=float(o)
						except :
							s2="error"
						
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
						s3="ER"
					elif 'O' in o : 
						s3="ER"
					elif ' ' in o : 
						s3="ER"
					
					else :
						try :
							s3=float(o)
						except :
							s3="error"
								
						if s3 > 1000 : 
							s3="ER"
					
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
						s4="ER"
					elif 'O' in o : 
						s4="ER"
					elif ' ' in o : 
						s4="ER"
					
					else :
						try : 
							s4=float(o)
							print "Done TRY"
						except : 
							s4="Error"
							if s4 > 1000 : 
								s4="ER"
					#print "s4 = " , s4
				
				print "==========================="
				print "The Fourth Sensor -ORP- Equal = ",s4
				print "==========================="
			
		



conn.close()
