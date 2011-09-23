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
    logging.debug("Sending headers: \n%s\n" % headers.decode())
    #logging.debug("host\n %s" %host) 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
#    s.settimeout(1)
    
    try :
        s.connect((host,int(port)))
    
    except Exception as err :
        logging.critical("Bad address/DNS for host: %s port: %s\n%s" % (host, port, err))
        s.close()
        #return buff
    
    try :
        s.sendall(headers)

    except Exception as err :
        #print(err)
        logging.critical(err)
        s.close()
        #return buff



    #s.shutdown(socket.SHUT_WR)
    while True :
       
        try :
            data = s.recv(1388)
            try : 
                # Some servers will not close (send 0 bytes) while write is open
                # Others will not send any data if write is shutdown before read.
                s.shutdown(socket.SHUT_WR)
            except Exception :
                pass
            #buff = buff + data
        except Exception as err :
            logging.warn("Problem reading from proxy socket. Closing:.\n%s" %err)
            s.close()
            return

        if len(data) == 0 : 
            logging.debug("Proxy read completed")
            break	

        client_socket.sendall(data)        
    logging.debug("Closing proxy socket")

    s.close()


