import socket
import sys
from os.path import basename

# To create a connection to a socket server
def createConnTo(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except:
		print 'Failed to create Socket'
		sys.exit()
	s.connect((host, port))
	return s

# To send a file to a socket server
def sendFile(sock, fil):
	try:
		data = fil.read(1024)
		while data != '':
			sock.sendall(data)
			data = fil.read(1024)
	finally:
		print 'File ' + basename(fil) + ' Sent'
		fil.close()

# To send a message to a socket server
def sendMsg(sock, msg):
	try:
		sock.sendall(msg)
	except socket.error:
		print 'Message Sending Failed'
		sys.exit()
	print 'Message Sent'

# To create a socket listener here
def createListenerHere(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.bind((host, port))
	except socket.error, msg:
		print 'Bind Failed. Errr Code : ' + str(msg[0]) + ' Message : ' + str(msg[1])
		sys.exit()
	return s