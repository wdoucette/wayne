#!/usr/bin/python3.2.2
""" Proxy socket client.

"""

import socket
import logging

def fetch(host, port, headers) :

    """ Returns fetched response of relayed headers.  

    """
    #TODO investigate MTU - seems to require 1388 ... can we auto detect?
    
    buff = bytes()
    
    logging.debug("csock connecting to host: %s port: %s" %(host, port))
    logging.debug("Sending headers: \n%s\n" %headers)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,int(port)))
    s.sendall(headers)

    while True :
        
        data = s.recv(1388)
        buff += data
        
        if len(data) < 1388 : 
            break	

    s.shutdown(socket.SHUT_WR)
    s.close()

    logging.debug(buff)
    return buff 

