#!/usr/bin/env python3
"""walkabout - demo. Usage:
walkabout.py <filename> -n{} [n lines] -t[tail] -i[invert]
"""

import io
import sys
import os
import getopt
import doctest

class Usage(Exception) :
    def __init__(self, msg) :
        self.msg = msg

def main(argv = None) :
    """main.__doc__ docstring"""

    doctest.testmod()

    invert, tail = False, False
    nlines = None
        
    # Parse command line arguments
    try :
        if argv is None : 
            argv = sys.argv 

        try :
            opts, args = getopt.getopt(sys.argv[1:], "-h-l:-t-iv", ["help"])    
       
        except getopt.error as err :
        
            raise Usage(err)

        for o, a in opts :

            if o in ("-h", "--help"):
                print(__doc__)
                exit(0)
            
            if o in ("-t") :
                tail = True
            if o in ("-i") :
                invert = True

            elif o in ("-l"):
                nlines = int(a)
                #exit(0)

        try : 
            filename=args[0]
        
        except IndexError as err :
            raise Usage("No filename provided.")

        walkabout(filename, nlines, myVar2, myVar3)

    except Usage as err:
        print("%s\n\n%s" %(err.msg, __doc__))


def walkabout(filename, nlines = None, tail = False, invert = False) :
    """
>>> walkabout("walkabout.py", 3)
#!/usr/bin/env python3
\"\"\"walkabout - demo. Usage:
walkabout.py <filename> -n{} [n lines] -t[tail] -i[invert]
"""
    buff = list()#[]
    lines = str()
    
    try :
        if os.path.isfile(filename) is None :
            
            raise Usage("File does not exist.")

        try :
            with io.open(filename, "r") as file :

                buff = file.readlines()
                
                if nlines == None : 
                    nlines = len(buff)
                
                if tail :
                    start = len(buff) - nlines
                    end = len(buff) 
                else :
                    start = 0
                    end = nlines
                
                buff = buff[start:end]

                if invert : buff.reverse()
                
                for line in buff : 
                    print(line, end="") 

        except IOError as err :

            print("IO Error({0})".format(err), file=sys.stderr)
            raise Usage(err)

    except Usage as err:
        print(err)
        return 2

if __name__ == "__main__" :
    sys.exit(main())


