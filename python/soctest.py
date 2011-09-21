#!/usr/bin/python3.2.2

"""Minimal ipv4 python socket server.

"""

import re
import socket
import io
import doctest
import getopt
import sys
import logging
import threading


class client_thread(threading.Thread) :

 
    #spawned for each client request.
    def enum(**enums):
        """ (**enums) notation expects f(var1=val1, var2=val2, ... ) 
            (*args) notation expects f(val1, val2, ... )
         #      >>> class X:
         #      ...     a = 1
         #      
         #      >>> X = type('X', (object,), dict(a=1))  

        """
        
        return type('Enum', (str,), enums) #type(name, bases, dict   )
    
    Services = enum(HTTPS='443', HTTP='80', FTP='21', IMAP='445', SSH='22')


    def __init__(self, clientsocket) :
        self.clientsocket = clientsocket
        

    def run(self) :
        buff_len = 1024
        buff = bytes()

        while True :
            
            data = self.clientsocket.recv(buff_len)
            buff += data
            logging.debug("Client thread read {0} byte chunk. {1} bytes total.".format(len(data), len(buff)) )
            
            if len(data) < buff_len : 
                break
            
            
       
        logging.debug("Client request received. Processing proxy request...")

        #logging.info(buff)
        # regex for requested /page
        #TODO GET | POST | ... ?
        #TODO implement header test cases.
        p = re.compile('GET (.*) HTTP(.*)')

        try :
            get_request = p.match(buff.decode('ascii')).group(1).strip()        
        except AttributeError :
            logging.critical("AttributeError in request header regex. %s" % buff )

        try :
            dic = self.parse_full_get(get_request)

        except RuntimeError as err :
            logging.critical("RuntimeError: %s" % err)
            exit(2) 
    
        proto = dic['proto']
        host = dic['host']
        port = dic['port']
        path = dic['path']


        if host == ""  :
            host = (re.search(r'Host: (.*)', buff.decode('ascii')).group(1)).split(':')[0]

        # Relay intact headers.
        content = self.get_page(host, port, buff)
        
        self.clientsocket.sendall(content)

        self.clientsocket.close()    

        logging.debug("Client thread completed.\n")
        
    #@staticmethod
    #@classmethod
    def parse_full_get(self, get_request) :

        """Determines protocol, host, port and filepath from HTTP GET request.
    # Example test cases:
        
        >>> mysock = mysocket
        >>> print(mysock.parse_full_get(mysock, "https://domain.com/"))
        {'path': '', 'host': 'domain.com', 'port': '443', 'proto': 'https'}
        
        >>> print(mysocket.parse_full_get(mysock, "http://mydomain.com:8081/path/to/file"))
        {'path': 'path/to/file', 'host': 'mydomain.com', 'port': '8081', 'proto': 'http'}

        >>> print(mysocket.parse_full_get(mysock, "127.0.0.1:8081/"))
        {'path': '', 'host': '127.0.0.1', 'port': '8081', 'proto': 'http'}

        >>> print(mysocket.parse_full_get(mysock, "/direct/request/relative/path"))
        Traceback (most recent call last):
        RuntimeError: Direct requests not allowed. Requested path was: direct/request/relative/path
        
    """

        #import logging
        dic = {}

        if get_request.find('/') == 0 :

            # Get request is relative to host/ , -not a proxied request.
            raise RuntimeError('Direct requests not allowed. Requested path was: %s' % get_request[1:])

        proto = get_request.split('://')[0]

        try :
            get_request = get_request.split('://')[1]

        except IndexError :

            # No protocol specified.
            proto = "http"
            logging.debug('No protocol specified, defaulting to %s.' % proto)

        hostport = get_request.split('/')[0]

        host = hostport.split(':')[0]

        try :
            port = hostport.split(':')[1]

        except IndexError :

            #if proto == 'http' : port = '80'
            #if proto == 'ftp' : port = '21'
            # ...
            
            # Build Services enum. TODO not sure if this is wise. 
            port = eval('self.Services.' + proto.upper() )

            logging.debug('No port specified, defaulting to %s.' % port)

        dic['host'] = host
        dic['path'] = get_request[get_request.find('/')+1:]
        dic['port'] = port
        dic['proto'] = proto

        return dic
    
    
    def get_page(self, host, PORT, headers) :

        # Client socket
        import csock
        return csock.fetch(host, PORT, headers)




class mysocket :
    
    def __init__(self) :
        """Initialize and configure program logging etc.

    """
        #if __name__ == '__main__' :
            
            # Log has to be setup before doctest
        self.initLog()
        doctest.testmod()
        
        
        # Establish proxy server on localhost:8081
        HOST = 'localhost' # None, '' ... Symbolic meaning all available interfaces
        PORT = 8081
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.setblocking(1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,5)

        s.bind((HOST, PORT))
        s.listen(5)


        
        #print("Conntectd by: ", address)
        #TODO thread for multiple requests, persist
        #TODO config file
        #DONE TODO opts
        #TODO mangle header
        #DONE log


        #open in binary write mode, no need to cast byte(ascii)
        f =open("/tmp/get","w+b")
        
        while True :
        
            # Server
            
            logging.debug("Socket server accepting requests.")
            (clientsocket, address)  = s.accept()
            
            # Spawn new client request.
            logging.debug("Request received. Spawing client processor...")
            ct = client_thread(clientsocket)
            ct.run()

            continue

        print(len(content))
        f.write(bytes(data,'ascii'))

    
    
    #@staticmethod
    def initLog(self):

        #logging.debug("Screw it") ... note to self: can't use logging before initalizing or its a no-op

        def usage() :

            print("""Usage:
        -h --help : this menu
        --verbosity= [ Info | Warn | Error | Debug ]
        -d log level DEBUG
        -l [filename] | --logfile=[filename]
        """)


        # Defaults
        
        log_level = 'info'
        logfile_name = ""

        try :
            opts, args = getopt.getopt(sys.argv[1:], '-h-d-l:v', ['help', 'verbosity=', 'logfile='])

        except getopt.GetoptError as err :

            logging.error(err)
            usage()
            exit(2)

        for o, a in opts :

            if o in ("-h", "--help"):
                usage()
                exit(0)

            if o in ("-d", "--verbosity"):

                if o == '-d' : a = 'DEBUG' # be verbose
                log_level = a.upper()
                #logging.debug("set logging to %s" %a.upper())
            
            if o in ("-l", "--logfile") :
                    # Set log level and log filename.
                logfile_name = a
                logfile_mode = 'w'

        # Apply log options.
        n_log_level= getattr(logging, log_level.upper(), None)
        if not isinstance(n_log_level, int):
                raise ValueError('Invalid log level: %s' % a)

        if logfile_name == "" :
            # Set log level only.
            logging.basicConfig(level=n_log_level)
            logging.info("Set log level %s" % log_level)
       
        else :
            # Set log level and filename    
            logging.basicConfig(filename=logfile_name, filemode=logfile_mode, level=n_log_level)
            logging.info("Set log level to %s and log file to %s" % (log_level, logfile_name))

        
        
            
            
        
mysock = mysocket() 


#initLog()
logging.debug("done init")




logging.debug("doing tests")


   






