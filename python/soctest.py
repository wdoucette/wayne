#!/usr/bin/python3.2.2

"""Minimal ipv4 python socket server.

"""

import socket
import sys
import io
import re


def parse_full_get(get_request) :

	"""Determines protocol, host, port and filepath from HTTP GET request.

# Example test cases: 
>>> print(parse_full_get("https://domain.com/"))
No port specified, defaulting.
{'path': '', 'host': 'domain.com', 'port': '443', 'proto': 'https'}

>>> print parse_full_get("http://mydomain.com:8081/path/to/file")
{'path': 'path/to/file', 'host': 'mydomain.com', 'port': '8081', 'proto': 'http'}

>>> print parse_full_get("127.0.0.1:8081/")
No protocol specified, defaulting to http.
{'path': '', 'host': '127.0.0.1', 'port': '8081', 'proto': 'http'}

>>> print parse_full_get("/direct/request/relative/path")
Traceback (most recent call last):
RuntimeError: Direct requests not allowed. Requested path was: direct/request/relative/path
"""
	dic = {}

	if get_request.find('/') == 0 :

		# Get request is relative to host/ , -not a proxied request.
		raise RuntimeError('Direct requests not allowed. Requested path was: %s' % get_request[1:])
	
	proto = get_request.split('://')[0]

	try :
		get_request = get_request.split('://')[1]

	except IndexError :

		# No protocol specified.
		print('No protocol specified, defaulting to http.')
		proto = "http"
	
	hostport = get_request.split('/')[0]
		
	host = hostport.split(':')[0]
	
	try :
		port = hostport.split(':')[1]

	except IndexError :

		print('No port specified, defaulting.')
		if proto == 'http' : port = '80'
		if proto == 'ftp' : port = '21'
		if proto == 'https' : port = '443'
		
	dic['host'] = host
	dic['path'] = get_request[get_request.find('/')+1:]
	dic['port'] = port
	dic['proto'] = proto

	return dic


if __name__ == "__main__":
	
	import doctest
	doctest.testmod()


# Establish proxy server on localhost:8081
HOST = 'localhost' # Symbolic meaning all available interfaces
PORT = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 5)
s.bind((HOST, PORT))
s.listen(5)
conn, recv = s.accept()
print("Conntectd by: ", recv)
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
		print(buff)
		# regex for requested /page
		p = re.compile('GET (.*) HTTP(.*)')
		try :
			get_request = p.match(data).group(1).strip()		
		except RuntimeError :
			exit(1)
		dic = parse_full_get(get_request)

		proto = dic['proto']
		host = dic['host']
		port = dic['port']
		path = dic['path']

			
		if host == ""  :
			host = (re.search(r'Host: (.*)', data).group(1)).split(':')[0]
		
		#regex for host:port
		#p = re.compile('Host: (.*)$',re.M)
		#.strip() is necessary to remove \r which comes before the \n -'$' 
		#addr = p.search(data).group(1).strip()

		#host = addr.split(':')[0]
	#	print("Host: %s" % host)
#		try :
#			port = addr.split(':')[1]
#		except IndexError :
#			port = 80	

		# fq path
	#	path = "Path: %s %s\n" % (host, page)
	

		print("proto: {0}".format(proto))
		print("host: {0}".format(host))
		print("port: {0}".format(port))
		print("path: {0}".format(path))
#	
		exit()	
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


