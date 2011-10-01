#!/usr/bin/env python3
"""Example getch module usage."""
import sys
import getch

def main() :
    
    # Empty stdin
    sys.stdin, data = getch.flush_fd(sys.stdin)
    if data: print(data)
    
    # Get next key press
    ch = getch.getch(True)
    print('got %s' %ch)


if __name__ == "__main__" :

    sys.exit(main())
