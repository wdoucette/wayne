#!/usr/bin/python3.2.2

"""Minimal ipv4 python socket server.

"""

import socket
import sys
import io
import re


# Establish proxy server on localhost:8081
HOST = 'localhost' # Symbolic meaning all available interfaces
PORT = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 5)
s.bind((HOST, PORT))
s.listen(5)
conn, recv = s.accept()

#TODO thread for multiple requests, persist
#TODO opts
#TODO mangle header
#TODO log


#open in binary write mode, no need to cast byte(ascii)
f =open("/tmp/get","w+b")
buff = ""
buff_len = 4096


def get_page(host, PORT, headers) :

	# Client socket
	import csock
	return csock.fetch(host, PORT, headers)

while True :

	data = conn.recv(buff_len)
	buff += data.decode('ascii')
	if (len(data) < buff_len) : # Buffer not full, end of stream. #if ( (not data) | (len(data)< buff_len)): 
	
		print("Request complete. Client SHUT stream. Replying...")

		data = buff
		
		# regex for requested /page
		p = re.compile('GET (.*) HTTP(.*)')
		page = p.match(data).group(1).strip()
		
		#p = re.compile('(.*\Z)', re.M)
		#request = p.match(data).group(1)
		#print(request)
		#print("REQUEST: {0}".format(request))	
			
	#	host= re.search(r'Host: (.*)', data).group(1)
		
		#regex for host:port
		p = re.compile('Host: (.*)$',re.M)
		#.strip() is necessary to remove \r which comes before the \n -'$' 
		host = p.search(data).group(1).strip()

		# fq path
		path = "%s%s" % (host, page)
	
		print("Resource path: %s" % (path))
		print("host: {0}".format(host))
		print("page: {0}".format(page))
		
		
		# relay intact headers
		headers = data
		content = get_page(host, 80, headers)
		

	
		#string = data #bytes(data,'ascii')#"Accept: text/html\n\rContetn-Encoding: gzip;bjzip"
		#print("Data {0}".format(data))
		
		#dic = {}
		#print("string: {0}".format(string.split('\r\n')))
		#for entry in string.split('\r\n') :
		#	key, value = entry.split(': ')
		#	dic[key] = value
			
		#print("Dictionary: {0}".format(dic))
		# Send ascii response as byte values

		conn.send(content)
		print("Sent {0} bytes".format(len(content)))
		break


conn.close()
print(len(content))
f.write(bytes(data,'ascii'))

