#!/usr/bin/python3
"""
This is a program that converts markdown to html
"""


import sys
from os.path import isfile

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    elif not isfile(sys.argv[1]):
        print (f"missing {sys.argv[1]}")
        sys.exit(1)
    else:
        sys.exit(0)
