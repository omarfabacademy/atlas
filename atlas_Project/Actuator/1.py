import socket


HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 12345             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1 :
	x = input("Please insert Number")
	if x == 1 : 
		conn.send('1')
	else : 
		conn.send('0')
