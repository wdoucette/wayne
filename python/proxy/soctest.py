#!/usr/bin/python3.2.2

"""ipv4 python proxy server.

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

    # Spawn for each client request.
    import csock

    count = 0
    def __init__(self, clientsocket) :
        
        self._initialized = True
        self._started = True

        self.clientsocket = clientsocket
        client_thread.count += 1
        
        logging.debug("Initializing thread. Current count: %i" %client_thread.count)

        # Manual init.
        # threading.Thread.__init__(self)        
        # Multiple inheritance, 'automatic' init
        super().__init__()

    def run(self) :
        
        buff_len = 4096
        buff = bytes()

        logging.debug('Waiting to read client request...')           
        
        while True :
            
            data = self.clientsocket.recv(buff_len)
            buff += data
            
            logging.debug("Client thread read {0} byte chunk. {1} bytes total.".format(len(data), len(buff)) )


            if len(data) < buff_len : 
                break
            
        if len(buff) == 0 :

            # Client abondoned socket.
            logging.warning('Client request 0 bytes, closing socket.')
            self.clientsocket.close()
            return
       
        logging.debug("Client request received. Processing proxy request...length: %s\n%s" %( len(buff), buff))

        # TODO we can arbitarily apply a codec here. Only header can be assumed ascii
        # the body (POST/PUT) etc must be stripped - delimited by \r\n\r\n
        #logging.debug("\n\nRaw client request buffer:\n%s" %buff.decode('utf-8'))
        
        #TODO GET | POST | ... ?
        #TODO implement header test cases.
        f = open("/tmp/buff", "a")
        f.write(buff.decode('utf-8'))
        dic = parse_request_header(buff)
        
        self.csock.fetch(dic['host'], dic['port'], dic['proxy_header'], self.clientsocket)
        
        logging.debug("Returned from client proxy, shutting down client socket thread")
        
        self.clientsocket.shutdown(socket.SHUT_RDWR)
        self.clientsocket.close()    

        logging.debug("Client thread completed.\n")
        client_thread.count -= 1
        

def parse_request_header(buff) :
        """ Extracts host, port, content length, content. 


# GET request
>>> buff = b"GET http://api.thetrafficstat.net/related?s=750&md=21&pid=473680971423164000&sess=773492173524573400&q=http%3A%2F%2Fdocs.python.org%2Flibrary%2Ffunctions.html&prev=http%3A%2F%2Fdocs.python.org%2Flibrary%2Fconstants.html&link=1&hreferer=http%3A%2F%2Fdocs.python.org%2Flibrary%2Fconstants.html HTTP/1.1\\r\\nHost: api.thetrafficstat.net\\r\\nProxy-Connection: keep-alive\\r\\nX-Requested-With: XMLHttpRequest\\r\\nUser-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30\\r\\nAccept: application/json, text/javascript, */*; q=0.01\\r\\nAccept-Encoding: gzip,deflate,sdch\\r\\nAccept-Language: en-US,en;q=0.8\\r\\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\\r\\nCookie: pid2=70727a560d5f1081; ASP.NET_SessionId=aenf3u45qt5efk55rqipg345\\r\\n\\r\\n"
>>> dic = parse_request_header(buff)
>>> print(dic['host'])
api.thetrafficstat.net
>>> print(dic['action'])
GET
>>> print(dic['path'])
/related?s=750&md=21&pid=473680971423164000&sess=773492173524573400&q=http%3A%2F%2Fdocs.python.org%2Flibrary%2Ffunctions.html&prev=http%3A%2F%2Fdocs.python.org%2Flibrary%2Fconstants.html&link=1&hreferer=http%3A%2F%2Fdocs.python.org%2Flibrary%2Fconstants.html

# POST request - writes parsed header in raw binary format
>>> buff = b"POST http://statcounter.com/project/ HTTP/1.1\\r\\nHost: statcounter.com\\r\\nProxy-Connection: keep-alive\\r\\nReferer: http://statcounter.com/\\r\\nContent-Length: 56\\r\\nCache-Control: max-age=0\\r\\nOrigin: http://statcounter.com\\r\\nUser-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30\\r\\nContent-Type: application/x-www-form-urlencoded\\r\\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\\r\\nAccept-Encoding: gzip,deflate,sdch\\r\\nAccept-Language: en-US,en;q=0.8\\r\\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\\r\\nCookie: landing=http%3A//statcounter.com/|||; login=wdoucette%26cae836e112dda0dc72402dfdd638947f; is_unique_1=sc5473791.1316073483.2; is_unique=sc3566826.1316073489.2-1417324.1315759362.1-1417516.1315759348.0-204609.1316644289.5\\r\\n\\r\\nform_user=wdoucette&form_pass=123456&LOGIN_BUTTON=LOGIN"

>>> buff = bytes(buff)
>>> dic = None
>>> dic = parse_request_header(buff)
>>> print(dic['host'])
statcounter.com
>>> print(dic['action'])
POST
>>> print(dic['path'])
/project/
>>> f =open("/tmp/out" , "w+b")
>>> f.write(dic['header'])
830
>>> f.close()
>>> print(dic['header'].decode())
POST http://statcounter.com/project/ HTTP/1.1\r\nHost: statcounter.com\r\nProxy-Connection: keep-alive\r\nReferer: http://statcounter.com/\r\nContent-Length: 56\r\nCache-Control: max-age=0\r\nOrigin: http://statcounter.com\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30\r\nContent-Type: application/x-www-form-urlencoded\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: gzip,deflate,sdch\r\nAccept-Language: en-US,en;q=0.8\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\nCookie: landing=http%3A//statcounter.com/|||; login=wdoucette%26cae836e112dda0dc72402dfdd638947f; is_unique_1=sc5473791.1316073483.2; is_unique=sc3566826.1316073489.2-1417324.1315759362.1-1417516.1315759348.0-204609.1316644289.5
>>> print(dic['body'])
b'form_user=wdoucette&form_pass=123456&LOGIN_BUTTON=LOGIN'


# Mangled header: No address for hostname.
#>>> s = mysocket() 
#>>> dic = None
#>>> buff = b'GET http://statcounter.comhttp//statcounter.com/project/?account_id=1748325&login_id=1&code=641e2527035d03cc200debd3b2fdb9db& HTTP/1.1\\r\\nHost: statcounter.comhttp\\r\\nProxy-Connection: keep-alive\\r\\nReferer: http://statcounter.com/\\r\\nCache-Control: max-age=0\\r\\nUser-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30\\r\\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\\r\\nAccept-Encoding: gzip,deflate,sdch\\r\\nAccept-Language: en-US,en;q=0.8\\r\\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\\r\\n\\r\\n'
#>>> dic = parse_request_header(buff)
#>>> content = get_page(dic['host'], dic['port'], buff)
[Errno -5] No address associated with hostname

"""     

        # TODO Separate request body from headers -e.g., PUT
#        logging.debug("content start: %i" %buff.find(r"\n\n")) 

        # Safe way to separate unknown content body encoding from known ascii header
        # Can be used for processing response header also.
        body = buff[buff.find(b'\r\n\r\n')+4:]
        header = buff[:buff.find(b'\r\n\r\n')]
        

        #logging.debug("Request Header: %s" % header.decode())
        #logging.debug("Request Body: %s" % body.decode())
        
        # Parse HTTP action.
        p = re.compile('([A-Z]*)[ ](.*) HTTP(.*)')
        
        try :
             action = p.match(buff.decode()).group(1)
       
        except AttributeError as err :
            
            logging.critical("AttributeError in ACTION header regex. %s\n%s" % (err, buff) )

        # Parse request. 
        try :
            
            request = p.match(buff.decode()).group(2).strip()        
        except AttributeError as err :
            logging.critical("AttributeError in REQUEST header regex. %s\n%s" % (err, buff) )
            exit(2)
            
        try :
            dic = parse_full_get(request)

        except RuntimeError as err :
            logging.critical("RuntimeError: %s" % err)
            exit(2) 
    
        dic['action'] = action
        
        # Rebuild first header line.
        regex = re.compile('[^\\n]*\\n(.*)', re.MULTILINE | re.DOTALL)
        
        proxy_headers = regex.search(buff.decode()).group(1)
        proxy_headers = bytes(dic['action'] +" " + dic['path'] +" " + "HTTP/1.1\r\n" + proxy_headers,'ascii')



        dic['proxy_header'] = proxy_headers
        dic['body'] = body
        dic['header'] = header

        #    host = (re.search(r'Host: (.*)', buff.decode('ascii')).group(1)).split(':')[0]
        logging.debug(dic['host'])
        logging.debug("\n\nProxied Request Header:")
        #logging.debug(dic['proxy_header'].decode('utf-8'))
        return dic

#@staticmethod
#@classmethod
def parse_full_get(request) :

    """Determines protocol, host, port and filepath from HTTP GET request.
# Example test cases:
    
    #>>> self = client_thread
    #>>> print(parse_full_get("https://domain.com/"))
    {'path': '', 'host': 'domain.com', 'port': '443', 'proto': 'https'}
    
    #>>> print(self.parse_full_get(self, "http://mydomain.com:8081/path/to/file"))
    {'path': 'path/to/file', 'host': 'mydomain.com', 'port': '8081', 'proto': 'http'}

    #>>> print(self.parse_full_get(self, "127.0.0.1:8081/"))
    {'path': '', 'host': '127.0.0.1', 'port': '8081', 'proto': 'http'}

    #>>> print(self.parse_full_get(self, "/direct/request/relative/path"))
    Traceback (most recent call last):
    RuntimeError: Direct requests not allowed. Requested path was: direct/request/relative/path
    
"""

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

  
    dic = {}

    if request.find('/') == 0 :

        # Get request is relative to host/ , -not a proxied request.
        raise RuntimeError('Direct requests not allowed. Requested path was: %s' % request[1:])

    proto = request[:request.find('://')]

    try :
        request = request[len(proto)+3:]

    except IndexError :

        # No protocol specified.
        proto = "http"
        logging.debug('No protocol specified, defaulting to %s.' % proto)

    hostport = request.split('/')[0]

    host = hostport.split(':')[0]

    try :
        port = hostport.split(':')[1]

    except IndexError :

        # Build Services enum. TODO not sure if this is wise. 
        port = eval('Services.' + proto.upper() )

        logging.debug('No port specified, defaulting to %s.' % port)

    dic['host'] = host
    #
    #
    #### TODO Path should become request
    dic['path'] = request[request.find('/'):]
    dic['port'] = port
    dic['proto'] = proto

    return dic

    
class mysocket :
    
    def __init__(self) :
        """Initialize and configure program logging etc.

    """
        #if __name__ == '__main__' :
            
            # Log has to be setup before doctest
        self.initLog()
        doctest.testmod()
        
        # TODO paramaterize server HOST/PORT        
        # Establish proxy server on localhost:8081
        HOST = 'localhost' # None, '' ... Symbolic meaning all available interfaces
        PORT = 8081
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.setblocking(1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((HOST, PORT))
        s.listen(5)

        #TODO config file

        #open in binary write mode, no need to cast byte(ascii)
        f =open("/tmp/get","w+b")
        
        while True :
        
            # Server
            
            logging.debug("Socket server accepting requests.")
            (clientsocket, address)  = s.accept()
            
            # Spawn new client request.
            logging.debug("Request received. Spawing client thread...")
            ct = client_thread(clientsocket)
            ct.start()
            
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

