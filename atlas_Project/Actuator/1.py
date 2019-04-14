import socket
import time

HOST = '10.42.0.1'                 # Symbolic name meaning all available interfaces
PORT = 1234             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1 :
	x = raw_input("Please insert Number")
	if x!='0' : 
		conn.send(x)
	else :
		while 1 :
			conn.send('2')
			time.sleep(2)
			conn.send('3')
			time.sleep(2)
			conn.send('4')
			time.sleep(2)
			conn.send('5')
			time.sleep(2)
			conn.send('6')
			time.sleep(2)
			conn.send('7')
			time.sleep(2)
			conn.send('8')
			time.sleep(2)
			conn.send('9')
			time.sleep(2)
			conn.send('10')
			time.sleep(2)
			conn.send('11')
			time.sleep(2)
			conn.send('12')
			time.sleep(2)
			conn.send('13')
			time.sleep(2)
			conn.send('14')
			time.sleep(2)
			conn.send('15')
			time.sleep(2)
			conn.send('16')
			time.sleep(2)
			conn.send('17')
			time.sleep(2)
			conn.send('18')
			time.sleep(2)
			conn.send('19')
			time.sleep(2)
			conn.send('1')
			time.sleep(2)
			
