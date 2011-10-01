#!/usr/bin/env python3
"""getch.py 
Try:
getch.py """

"""getch.py Copyright 2011 Wayne Doucette."""

import os
import io
import sys
import getopt
import doctest
import subprocess

class Usage(Exception) :

    def __init__(self, msg) :
        self.msg = msg

def main(argv = None) :
    """Non-blocking non-buffered / blocking non-buffered read from stdin. 
Usage:
>>> main()

"""
    if argv is None :
        argv = sys.argv

    __initOpts(argv)

    sys.stdin, data = _flush_fd(sys.stdin)

    if data == None : print("stdin is a tty")
    else:    
        print("stdin data:\n%s" % data)
   
    getch = _Getch()
    
    print("Waiting for keypress.")
    ch = getch.__call__(True)
    print(ch)

def _flush_fd(fd) :
    """ If fd is a pipe, buffers data, then restores fd to tty and 
    returns buffer."""
    if not fd.isatty() :
        string = ""
        for lines in fd:
            string += lines

        # Find shell tty 
        p = subprocess.Popen(['tty'], stdin=sys.stderr, stdout=subprocess.PIPE)
        stdoutdata, stderrdata = p.communicate()
        pty = bytes(stdoutdata).decode()[:-1]

        #print("pty: %s" % pty)
        # Set stdin to console. 
        fd = open(pty,'r')
        return fd, string
    else : 
        return fd, None

class _Getch() :
 
    
    def __init__(self):

        try :
            self._getch = self._GetchMS()
        except ImportError :
            self._getch = self._GetchUnix()

    def __call__(self, blocking):
   
        self._getch.blocking = blocking
    
        
        return self._getch()

    class _GetchMS :

        def __init__(self):
            import msvcrt
        def __call__(self):
            import msvcrt
            return msvrt.getch()
        

    class _GetchUnix :

        def __init__(self) :
            self.blocking = False

        def __call__(self) :

            import termios
            import fcntl
            import sys  
        
            print('Blocking: %s' %self.blocking)
            fd = sys.stdin.fileno() #os.fdopen(0, "r",1) #sys.stdin.fileno()
            try :
                oldterm = termios.tcgetattr(fd)
                newattr = termios.tcgetattr(fd)
                newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
                termios.tcsetattr(fd, termios.TCSANOW, newattr)

                oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
                fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
            except Exception as err:
                print(err)
                pass
            try:
                while 1:
                    c = sys.stdin.read(1) #sys.stdin.read(0)
                    if c : 
                        break  
                    if self.blocking == False: 
                        break 
                        #if ord(c) == 10 :
            except IOError as err: 
                print(err)
                pass
            try : 
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
                fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
            except Exception as err: 
                print(err)
            return c 

class Getch() :   
    # Non - buffering getch()
    
    def __init__(self):
    
        self.getch = _Getch().__call__


def __initOpts(argv) :

    try : 
        try :
            opts, args = getopt.getopt(argv[1:], "hv", ["help"])

        except getopt.error as msg:
            raise Usage(msg)
        for o, a in opts :
            if o in ("-h", "--help") :
                raise Usage("")

        for arg in args :
            pass
    
    except Usage as err :
        print(__doc__, file=sys.stderr)
        exit(0)
 

if __name__ == "__main__" :
   
    #doctest.testmod()
    sys.exit(main())

else :
    getch = Getch().getch
    flush_fd = _flush_fd
