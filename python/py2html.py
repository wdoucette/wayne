#!/usr/bin/env python3
"""py2html.py - Format python source text in HTML: 
Try:
py2html.py [ infile | "raw python source text" | < stdin ] """

"""py2html.py Copyright 2011 Wayne Doucette."""

import os
import io
import sys
import doctest

class Usage(Exception) :

    def __init__(self, msg) :
        if msg : print(msg)
        print(__doc__, file=sys.stderr)
        Exception.__init__(self,msg)

def main(argv = None) :
    """
"""
    if argv is None :
        argv = sys.argv
    try:
        try:
            if "-h" in argv[1] :
                raise Usage("")
            if not sys.stdin.isatty() :
                py2html(sys.stdin, sys.stdout, "    ")
            else :
                py2html(argv[1], sys.stdout, "    ")
     
        except IndexError :
            raise Usage("No input provided.")
    except Usage as e :
        exit(0)
class py2html() :
    """
    >>> test = py2html("def myf :\
                if arg <> myval :\
                    pass", sys.stdout, '    ')
    <code type="text/python3">
    def myf :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if arg &lt;&gt; myval :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pass
    </code>
    """
    def __init__(self, src, dst, sep) :
        
        tab = "&nbsp;&nbsp;&nbsp;&nbsp;"
        
        if type(src) == str :
            try :
                src = open(src, 'r') #if hasattr(src, 'read') :
                src = src.read()
            except IOError :
                pass #raise Usage("Invalid filename")
        html = htmlencode(src)
        html = html.replace(sep, tab)
       
        print('<code type="text/python3">')
        print(html)
        print("</code>")

def htmlencode(html):
    
    items = [{'&':'&amp;'}, {'<':'&lt;'}, {'>':'&gt;'}, {'\n':'<br />'} ]
    
    for item in items:
        for chars in item:
            html = html.replace(chars, item[chars])
    return html

if __name__ == "__main__" :
   

    doctest.testmod()
    sys.exit(main())



