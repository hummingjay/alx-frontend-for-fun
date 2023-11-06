#!/usr/bin/python3
"""
This is a program that converts markdown to html
"""


import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
