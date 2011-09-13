#!/usr/bin/python3
import io, sys

"""pycat writes a file's content to stdout. Usage: pycat.py filename"""


if len(sys.argv) < 2 :
    exit(2)
    raise SystemExit("No filename provided. Try: pycat.py filename")

try :
	
    with io.open(sys.argv[1], "r") as file :

        buff = file.read()
        sys.stdout.write(buff)
        exit(0)
        
except IOError as err :
    
    sys.exit("IO Error({0})".format(err))
