#!/usr/bin/python3.2.2
"""Client for transparent proxy.

"""

import socket


#TODO investigate buff size max -mtu 1388? is there a way to detect?

def fetch(host, PORT, headers) :

#	print("HOST: {0}".format(host))
#	print("PORT: {0}".format(PORT))
#	print("headers: {0}".format(headers))

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,PORT))
	s.send(bytes(headers,'ascii'))
	#s.shutdown(socket.SHUT_WR)

	buff = bytes()
	while True :
		data = s.recv(1388)
		#print(data)
		buff += data#.decode('UTF-8')
		if len(data) < 1388 : break	
		
	
	#print("Data len: {0} ".format((buff)))
	return buff 

