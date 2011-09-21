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
    s.connect((host,int(PORT)))
    s.sendall(headers)

    buff = bytes()
    while True :
        data = s.recv(1024)
        #print(data)
        buff += data#.decode('ascii')
        if len(data) < 1024 : break	


    #print("Data len: {0} ".format((buff)))

    s.shutdown(socket.SHUT_WR)
    s.close()
    return buff 

