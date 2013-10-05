# Contains all the functions excluding the main image processing part (which is in serin.py)

import socket
import sys
from os.path import basename
import Tkinter, tkFileDialog


def printDone():
	print '-------------------------------'
	print '||||||    ||||   |\\  || ||||||'
	print '||   ||  ||  ||  ||\\ || ||    '
	print '                          ||>  '
	print '||   ||  ||  ||  || \\|| ||    '
	print '||||||    ||||   ||  \|| ||||||'
	print '-------------------------------'

def printSerin():
	print '--------------------------------------------------'
	print ' ________    ________    ______     _    __     _ '
	print '|  ______|  |  ______|  |  __  |   | |  |  \   | |'
	print '| |______   | |___      | |__| |   | |  |   \  | |'
	print '|______  |  |  ___|     |  __ |    | |  | |\ \ | |'
	print ' ______| |  | |______   | |  \ \   | |  | | \ \| |'
	print '|________|  |________|  |_|   \_\  |_|  |_|  \___|'
	print '--------------------------------------------------'

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

# To create a socket server here
def createListenerHere(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.bind((host, port))
	except socket.error, msg:
		print 'Bind Failed. Errr Code : ' + str(msg[0]) + ' Message : ' + str(msg[1])
		sys.exit()
	return s

# The main action function. Called when event happens.
def act(serverip, imsender = 0):
	conSock = createConnTo(serverip, 444) 
	print 'Connected to Server'

	# Asking for server status
	sendMsg(conSock, 'status_of_server')
	print 'Asking status of server'
	reply = conSock.recv(1024)
	conSock.close()
	if reply == 'send_file':
		print 'Ok, now I am sender'
		# Choosing file
		root = Tkinter.Tk()
		root.withdraw()
		toSend = tkFileDialog.askopenfilename()
		toSendName = basename(toSend)
		print 'You have selected ' + toSendName
		conSock = lib.createConnTo(server, 444)
		# Sending Filename to server
		sendMsg(conSock, toSendName)
		reply = conSock.recv(1024)
		if reply == 'ok':
			print 'Sent filename to server'
			imsender = 1
		conSock.close()
	if reply:
		# I m sender and i m broadcasting the file for reception
		if imsender == 1:
			filesender = createListenerHere('', 5555)
			filesender.listen(1)
			print 'Listening for file request'
			while True:
				conn, adr = filesender.accept()
				print 'Connected to ' + adr[0] + ':' + str(adr[1])
				req = conn.recv(1024)
				if req == 'gimme':
					print 'Connection asked for file, sending now.'
					toSendFile = open(toSend, 'rb')
					sendFile(conn, toSendFile)
					break
			printDone()
		
		# I m receiver and m asking sender for file
		else:
			print 'I m receiver, got file name and sender ip'
			replies = reply.split(',')
			fileName = replies[0]
			sender = replies[1]
			sockToFS = createConnTo(sender, 5555)
			fil = open(fileName, 'wb')
			print 'Requesting sender for file'
			sendMsg(sockToFS, 'gimme')
			response = sockToFS.recv(1024)
			while response != '':
				fil.write(response)
				response = sockToFS.recv(1024)
			fil.close()
			print 'File ' + fileName + ' received.'
			sockToFS.close()
			printDone()