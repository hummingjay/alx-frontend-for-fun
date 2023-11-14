#!/usr/bin/python3
"""
This is a program that converts markdown to html
"""


import sys
from os.path import isfile

if __name__ == "__main__":
    count = 0
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    elif not isfile(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    # To read the file
    with open(sys.argv[1], 'r') as f:
        target = open(sys.argv[2], 'w')
        html = f.readlines()

        in_list = False

        for x in html:
            '''
            method that returns True if the input string
            starts with the specified prefix(string): rstrip
            '''
            # Check the headings
            if x.startswith('#'):
                # rstrip remove trailing line
                text = x.rstrip()
                if x.startswith('######'):
                    line = ("<h6>" + text[7::1] + "</h6>" + "\n")
                    target.write(line)
                elif x.startswith('#####'):
                    line = ("<h5>" + text[6::1] + "</h5>" + "\n")
                    target.write(line)
                elif x.startswith('####'):
                    line = ("<h4>" + text[5::1] + "</h4>" + "\n")
                    target.write(line)
                elif x.startswith('###'):
                    line = ("<h3>" + text[4::1] + "</h3>" + "\n")
                    target.write(line)
                elif x.startswith('##'):
                    line = ("<h2>" + text[3::1] + "</h2>" + "\n")
                    target.write(line)
                elif x.startswith('#'):
                    line = ("<h1>" + text[2::1] + "</h1>" + "\n")
                    target.write(line)

                character = x
            # check for unordered list
            elif x.startswith('-'):
                if not in_list:
                    target.write("</ul>\n")
                    in_list = True

                text = x.rstrip()
                line = ("<li>" + text[2::1] + "</li>" + "\n")
                target.write(line)
                character = x
            elif in_list and character.startswith('-'):
                target.write("</ul>\n")
                target.write(x)
            else:
                target.write(x)
                character = x
        if in_list:
            target.write("</ul>\n")
        target.close()
    sys.exit(0)
