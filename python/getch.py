#!/usr/bin/env python3
"""getch.py Usage:
Try:
getch.py """

"""getch.py Copyright 2011 Wayne Doucette."""


import os
import io
import sys
import getopt
import doctest

class Usage(Exception) :

    def __init__(self, msg) :
        self.msg = msg


def main(argv = None) :

    """ Non buffering & Non blocking/Non buffering read from stdin. 
Usage:
>>> main()

"""
    if argv is None :
        argv = sys.argv

    __initOpts(argv)
    
    # Non - buffering getch()
    getch = __Getch()
    ch = getch.__call__()
    if ch : 
        print(ch)

    # Non - blocking and Non - buffering getch()




class __Getch() :
 
    
    def __init__(self):

        try :
            self._getch = self._GetchMS()
        except ImportError :
            self._getch = self._GetchUnix()

    def __call__(self):
       
        return self._getch()

   
    class _GetchMS :

        def __init__(self):
            import msvcrt
            def __call__(self):
                import msvcrt
                self._getch(self)
        

    class _GetchUnix :
        
        def __init__(self) :
            import termios, sys,io,os, tty

        def __call__(self) :

            import termios, sys,io,os, tty

            ch = None
            fd = 0 

            old = termios.tcgetattr(fd)
            new = termios.tcgetattr(fd)
            new[3] = new[3] & ~termios.ECHO # lflags
            try :
                termios.tcsetattr(fd, termios.TCSADRAIN,new)
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return ch



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
        return 2
 



if __name__ == "__main__" :
   
    #doctest.testmod()
    sys.exit(main())


