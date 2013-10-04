import socket
import sys
import lib

# Opening Socket
#--------------------------
HOST = ''
PORT = 444
print '--------------------------------------------------'
print ' ________    ________    ______     _    __     _ '
print '|  ______|  |  ______|  |  __  |   | |  |  \   | |'
print '| |______   | |___      | |__| |   | |  |   \  | |'
print '|______  |  |  ___|     |  __ |    | |  | |\ \ | |'
print ' ______| |  | |______   | |  \ \   | |  | | \ \| |'
print '|________|  |________|  |_|   \_\  |_|  |_|  \___|'
print '--------------------------------------------------'

serv = lib.createListenerHere(HOST, PORT)
serv.listen(10)
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
		# The client asks for state
		if data == 'status_of_server':
			print 'Client asked for state of server.'
			if filename == '':
				# The client is sender and is requested to give the file name.
				conn.sendall('send_file')
				print 'Asked client for file'
			else:
				# The client is reciever. File name and sender ip is sent to it.
				print 'Sent client the file details'
				conn.sendall(filename + ',' + sender)
				filename = ''
				sender = ''
		else:
			# The sender gives the file name.
			print 'Client sent the file name : ' + data
			if filename == '':
				conn.sendall('ok') # Informing sender that the file is noted for sending.
				filename = data
				sender = adr[0]

#--------------------------

conn.close()
serv.close()