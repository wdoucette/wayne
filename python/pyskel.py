#!/usr/bin/env python3

"""pyskel - Make a Python skeleton file.
Usage:
pyskel < filename >
"""

import os
import sys
import getopt
import stat
import pycat

class FuckYou(Exception) :

    def __init__(self, msg) :
        self.msg = msg
        self.usage = """
Try:
-fucking yourself"""


class Usage(Exception) :

    def __init__(self, msg) :
        self.msg = msg
        self.usage = """
Try:
pyskel <filename>"""

def main(argv = None) :
    """fuck me, you are a useless piece of dog shit."""  
    if argv is None :
        argv = sys.argv
    
    try: 
        try :
            opts, args = getopt.getopt(argv[1:], "h", ["help"])

        except getopt.error as msg:
            raise Usage(msg)
        for o, a in opts :
            if o in ("-h", "--help") :
                raise Usage("")
                
        filename =args[0]
   
        shabang = "#!/usr/bin/env python3"
        docstr = """
\"\"\"{0} Usage:
Try:
{0} <options> \"\"\"

\"\"\"{0} Copyright 2011 Wayne Doucette.\"\"\"
""".format(filename)

        content = shabang + docstr + """

import os
import sys
import getopt
import doctest


class Usage(Exception) :

    def __init__(self, msg) :
        self.msg = msg

def main(argv = None) :

    \"\"\">>> main()
Hello, World. This is {0}.
\"\"\"
    
    if argv is None :
        argv = sys.argv

    try : 
        try :
            opts, args = getopt.getopt(argv[1:], "h", ["help"])

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
        
    print("Hello, World. This is {0}.")



if __name__ == "__main__" :
   
    sys.exit(main())

doctest.testmod()

""".format(filename)


        # TODO make portable.
        if os.path.isfile("./%s" %filename) :

            print("The fucking FILE already exists, beotch!")
            print("...")
            pycat.pycat(filename, 4)
            print("...")

            if not input("\nProceed with overwriting file? ").upper() in ("Y", "YES", "YEP", "JA", "DA", "OUI", "OK", "SURE", "OO") :

                raise FuckYou("Mission aborted, pussy.")

        f = open("%s" %filename, "w")
        f.write(content)
        f.close()

        os.chmod(filename, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR | stat.S_IROTH)
        # TODO this is NOT portable.
        pycat.pycat(filename)
        #os.system("./%s -v | less" %filename) 
        #os.system("vi ./%s" %filename)
    
    except Usage as err :
            print("%s\n%s" %(err.msg, __doc__))
            return 2
    except (FuckYou, Exception) as fuck :
        print("%s" %(fuck.msg))
if __name__ == "__main__" :

    sys.exit(main())
