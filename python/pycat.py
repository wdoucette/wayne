#!/usr/bin/env python3
"""pycat - write a file to stdout. Usage:
pycat.py <filename> -n{} [n lines] -i [invert]
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
    nlines =0 
    invert = False

    try :
        if argv is None : 
            argv = sys.argv 

        try :
            opts, args = getopt.getopt(sys.argv[1:], "-h-l:-i", ["help"])    
       
        except getopt.error as err :
        
            raise Usage(err)

        for o, a in opts :

            if o in ("-h", "--help"):
                print(__doc__)
                exit(0)
            
            if o in ("-i") :
                invert = True

            elif o in ("-l"):
                nlines = int(a)
                #exit(0)

        try : 
            filename=args[0]
        
        except IndexError as err :
            raise Usage("No filename provided.")

        pycat(filename, nlines, invert)

    except Usage as err:
        print("%s\n\n%s" %(err.msg, __doc__))


def pycat(filename, nlines = 0, invert = False) :
    """
>>> pycat("pycat.py", 3)
#!/usr/bin/env python3
\"\"\"pycat - write a file to stdout. Usage:
pycat.py <filename> -n{} [n lines] -i [invert]
"""
    buff = ""

    try :
        if os.path.isfile(filename) is None :

            raise Usage("File does not exist.")

        try :

            with io.open(filename, "r") as file :
                if not nlines == 0:
                    while nlines :
                        line = file.readline()
                        if invert : 
                            buff = line + buff
                        else :
                            buff += line 
                        nlines -= 1

                    sys.stdout.write(buff)
                else :
                    buff = file.read()
                    sys.stdout.write(buff)
                    print()
                return #buff

        except IOError as err :

            print("IO Error({0})".format(err), file=sys.stderr)
            raise Usage(err)

    except Usage as err:
        print(err)
        return 2

if __name__ == "__main__" :
    sys.exit(main())
