#!/usr/bin/python3.2.2
""" Proxy socket client.

"""

import socket
import logging

def fetch(host, port, headers, client_socket) :


    """ Returns response to proxy request.  

    """
    
    buff = bytes()
    
    logging.info("Establishing connection to remote host %s:%s" %(host, port))
    logging.info("Sending request: \n%s\n" % headers.decode())
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    try : s.connect((host, int(port)))
    
    except Exception as err :
        
        logging.critical("Address/DNS error for host: %s port: %s\n%s" % (host, port, err))
        s.close()
        return -1

    # Send request to remote host.
    try : s.sendall(headers)

    except Exception as err :
        
        logging.critical(err)
        s.close()
        return -1

    while True :
       
        try : 
            # Receive a chunk of data from remote host.
            data = s.recv(4096)
       
            try : 
                # Some servers will not close (send 0 bytes) while write is open.
                # Others will not send any data if write is shutdown before a read.
                # So we read first, then shutdown writing from our end.
                s.shutdown(socket.SHUT_WR)
            
            except Exception : pass
        
        except Exception as err :
    
            logging.warn("Problem reading from remote host socket. Closing:.\n%s" %err)
            return -1

        if len(data) == 0 : 
            
            logging.info("Remote host finished sending.")
            s.close()
            return -1	
    
        # Send this data chunk to client.
        try : client_socket.sendall(data)        
        
        except Exception as err :
        
            logging.warn(err)
        
    # Repeat while loop until s.recv() returns 0 bytes.

    
    logging.info("Closing proxy connection to remote.")
    
    s.close()
    return 0

