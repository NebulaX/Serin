import socket
import sys
import lib
import Tkinter, tkFileDialog
from os.path import basename

server = '127.0.0.1' # Point it to server

conSock = lib.createConnTo(server, 444) 
print 'Connected to Server'

# Listen to Event here
#--------------------------
eventHappened = 0 # Set it to 1 when event happens
###########################
#--------------------------

imsender = 0 # Am I sender ???

if eventHappened == 1:
	# Asking for server status
	lib.sendMsg(conSock, 'status_of_server')
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
		lib.sendMsg(conSock, toSendName)
		reply = conSock.recv(1024)
		if reply == 'ok':
			print 'Sent filename to server'
			imsender = 1
		conSock.close()

if eventHappened == 1 and reply:
	# I m sender and i m broadcasting the file for reception
	if imsender == 1:
		filesender = lib.createListenerHere('', 5555)
		filesender.listen(1)
		print 'Listening for file request'
		while True:
			conn, adr = filesender.accept()
			print 'Connected to ' + adr[0] + ':' + str(adr[1])
			req = conn.recv(1024)
			if req == 'gimme':
				print 'Connection asked for file, sending now.'
				toSendFile = open(toSend, 'rb')
				lib.sendFile(conn, toSendFile)
				break
	
	# I m reciever and m asking sender for file
	else:
		print 'I m reciever, got file name and sender ip'
		replies = reply.split(',')
		fileName = replies[0]
		sender = replies[1]
		sockToFS = lib.createConnTo(sender, 5555)
		fil = open(fileName, 'wb')
		print 'Requesting sender for file'
		lib.sendMsg(sockToFS, 'gimme')
		response = sockToFS.recv(1024)
		while response != '':
			fil.write(response)
			response = sockToFS.recv(1024)
		fil.close()
		print 'File ' + fileName + ' recieved.'
		sockToFS.close()