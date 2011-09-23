#!/usr/bin/python3.2.2
""" Proxy socket client.

"""

import socket
import logging

def fetch(host, port, headers, client_socket) :


    """ Returns fetched response of relayed headers.  

    """
    #TODO investigate MTU - seems to require 1388 ... can we auto detect?
    
    buff = bytes()
    
    logging.debug("csock connecting to host: %s port: %s" %(host, port))
    #logging.debug("Sending headers: \n%s\n" %headers)
    #logging.debug("host\n %s" %host) 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        s.connect((host,int(port)))
    
    except Exception as err :
        logging.critical("Bad address/DNS for host: %s port: %s\n%s" % (host, port, err))
        s.close()
        return buff
    
    try :
        s.sendall(headers)
    except Exception as err :
        #print(err)
        logging.critical(err)
        s.close()
        return buff


    while True :
        
        data = s.recv(1388)
        buff += data

        client_socket.sendall(data)        
        
        if len(data) < 1388 : 
            break	

    #s.shutdown(socket.SHUT_RDWR)
    s.close()

    #logging.debug("Response received:\n%s" % buff)
    return buff 

