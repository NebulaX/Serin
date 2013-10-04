import socket
import sys
import lib

# Opening Socket
#--------------------------
HOST = ''
PORT = 444
print '. : S E R I N : . : S E R V E R : .'

serv = lib.createListenerHere(HOST, PORT)
serv.listen(1) # One Request to avoid mishappens
print 'Socket Listening'
#--------------------------

# The variables to store file and sender info
filename = ''
sender = ''

# Transaction management
#--------------------------
while True:
	conn, adr = serv.accept()
	print 'Connected to ' + adr[0] + ':' + str(adr[1])
	data = conn.recv(1024)
	if data != '':
		# If the client is the sender
		if filename == '':
			conn.sendall('ok') # Informing client that its file is noted for sending
			filename = data
			sender = adr[0]
		# If the client is the reciever
		else:
			conn.sendall(filename + ',' + sender) # Sending the sender and file details to reciever
			filename = ''
			sender = ''

#--------------------------

conn.close()
serv.close()