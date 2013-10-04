import socket
import sys
import lib

conSock = lib.createConnTo('127.0.0.1', 444)

# Add file to send here
#--------------------------
toSend = 'atx.jpg'
###########################
#--------------------------

# Listen to Event here
#--------------------------
eventHappened = 0
###########################
#--------------------------

if eventHappened == 1:
	lib.sendMsg(conSock, toSend) # Send filename to server
	reply = conSock.recv(1024)
	conSock.close()

if reply:
	# If server is free (no file to be sent)
	if reply == 'ok':
		filesender = lib.createListenerHere('', 5555)
		filesender.listen(1)
		print 'Listening for file request'
		while True:
			conn, adr = filesender.accept()
			req = conn.recv(1024)
			if req == 'gimme':
				toSendFile = open(toSend, 'rb')
				lib.sendFile(conn, toSendFile)
				break
	# When server has a pending file to send
	else:
		replies = reply.split(',')
		fileName = replies[0]
		sender = replies[1]
		sockToFS = lib.createConnTo(sender, 5555)
		fil = open(fileName, 'wb')
		lib.sendMsg(sockToFS, 'gimme')
		response = sockToFS.recv(1024)
		while response != '':
			fil.write(response)
			response = sockToFS.recv(1024)
		fil.close()
		print 'File ' + fileName + ' recieved.'
		sockToFS.close()