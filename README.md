
# alx-frontend-for-fun

## Markdown to HTML

---

## Tasks

### 0. Start a script

Write a script `markdown2html.py` that takes an argument 2 strings:

  First argument is the name of the Markdown file
  Second argument is the output file name

Requirements:

  If the number of arguments is less than 2: print in STDERR `Usage: ./markdown2html.py README.md README.html` and exit 1
  If the Markdown file doesn’t exist: print in STDER `Missing <filename>` and exit 1
  Otherwise, print nothing and exit 0

```
guillaume@vagrant:~/$ ./markdown2html.py
Usage: ./markdown2html.py README.md README.html
guillaume@vagrant:~/$ echo $?
1
guillaume@vagrant:~/$
guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
Missing README.md
guillaume@vagrant:~/$ echo $?
1
guillaume@vagrant:~/$
guillaume@vagrant:~/$ echo "Test" > README.md
guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ 
```

### 1. Headings

```
guillaume@vagrant:~/$ cat README.md
# My title
## My title2
# My title3
#### My title4
### My title5

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<h2>My title2</h2>
<h1>My title3</h1>
<h4>My title4</h4>
<h3>My title5</h3>
guillaume@vagrant:~/$ 
```

### 2. Unordered listing

Improve `markdown2html.py` by parsing Unordered listing syntax for generating HTML:

__Syntax__: (you can assume it will be strictly this syntax)

Markdown:

```
- Hello
- Bye
```

HTML generated:

```
<ul>
    <li>Hello</li>
    <li>Bye</li>
</ul>
```

```
guillaume@vagrant:~/$ cat README.md
# My title
- Hello
- Bye

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ul>
<li>Hello</li>
<li>Bye</li>
</ul>
guillaume@vagrant:~/$ 
```

Spacing and new lines between HTML tags don’t need to be exactly this one
