
# Sass & Scss

### Resources

 - [Sass Basics](https://sass-lang.com/guide/)
 - [Sass flow control directives: @if, @for, @each and @while](https://sass-lang.com/documentation/at-rules/control/while/)
 - [Sass references](https://sass-lang.com/documentation/)

### More Info

#### Comments for your Scss file:

__All your Scss file must start with a comment block__

```
$ cat my_styles.scss
/* My style */
body {
    .container {
        color: #3D3D3D;
    }
}
$
```

#### Install Sass/Scss on Ubuntu 18.04 LTS

```
$ sudo apt-get install -y ruby2.5 ruby2.5-dev
$ sudo apt-get install ubuntu-dev-tools
$ gem install sass -v 3.7.4
$ sass --version
Ruby Sass 3.7.4
```


## Tasks

### 0. Always debugging!

Write a Sass file that prints `Hello world` in the debug output.

```
guillaume@ubuntu:~/$ sass 0-debug_log.scss | head -n 0
0-debug_log.scss:2 DEBUG: Hello world
guillaume@ubuntu:~/$ 
```

File: [0-debug_log.scss](0-debug_log.scss)

### 1. Color variable

Write a Sass file that assigns the text color `#3D3D3D` to the HTML tags `body` and `p`.

 - You must use a Sass variable

```
guillaume@ubuntu:~/$ sass 1-color_variable.scss | tail -n +2
body {
  color: #3D3D3D; }

p {
  color: #3D3D3D; }
guillaume@ubuntu:~/$ 
```

File: [1-color\_variable.scss](1-color_variable.scss)

### 2. Colors

Write a Sass file that assigns:

 - The text color `#3D3D3D` to the HTML tags `body` and `p`
 - The background color `#6D6D6D` to the HTML tags `body` and `h2`
 - You must use 2 Sass variables

```
guillaume@ubuntu:~/$ sass 2-color_variables.scss | tail -n +2
body {
  color: #3D3D3D;
  background-color: #6D6D6D; }

p {
  color: #3D3D3D; }

h2 {
  background-color: #6D6D6D; }
guillaume@ubuntu:~/$ 
```

File: [2-color\_variables.scss](2-color_variables.scss)

### 3. Nested tag
Write a Sass file that assigns:

 - No margin or padding in body tags
 - Margin 10px to all of the p tags inside body tags
 - You must use nested declarations

```
guillaume@ubuntu:~/$ sass 3-nested_tag.scss | tail -n +2
body {
  margin: 0px;
  padding: 0px; }
  body p {
    margin: 10px; }
guillaume@ubuntu:~/$ 
```

File: [3-nested\_tag.scss](3-nested_tag.scss)

### 4. Nested class

Write a Sass file that assigns:

 - Text color #3D3D3D to elements inside body tags
 - Text color #FF0000 to any elements of class .red inside body tags
 - You must use nested declarations

```
guillaume@ubuntu:~/$ sass 4-nested_class.scss | tail -n +2
body {
  color: #3D3D3D; }
  body .red {
    color: #FF0000; }
guillaume@ubuntu:~/$ 
```

File: [4-nested\_class.scss](4-nested_class.scss)

### 5. Nested child
Write a Sass file that assigns:

 - Text color #3D3D3D to elements inside body tags
 - Text color #FF0000 to any elements of class .red that are the first children of the body
 - You must use nested declarations

```
guillaume@ubuntu:~/$ sass 5-nested_child.scss | tail -n +2
body {
  color: #3D3D3D; }
  body > .red {
    color: #FF0000; }
guillaume@ubuntu:~/$ 
```
File: [5-nested\_child.scss](5-nested_child.scss)

`
### 6. Nested hover

Write a Sass file that assigns:

 - Text color `#FF0000` to `button` tags
 - When the user hovers over `button` tags, text color should change to `#00FF00`
 - You must use nested declarations

```
guillaume@ubuntu:~/$ sass 6-nested_hover.scss | tail -n +2
button {
  color: #FF0000; }
  button:hover {
    color: #00FF00; }
guillaume@ubuntu:~/$ 
```

File: [6-nested\_hover.scss](6-nested_hover.scss)

### 7. Nested and nested again

Write a Sass file that assigns:

 - Font size 14px to all body tags
 - Font size 16px to all h1 tags inside body tags
 - Font size 12px to h1 tags of class .smaller inside body tags
 - You must use nested declarations

```
guillaume@ubuntu:~/$ sass 7-nested_deeper.scss | tail -n +2
body {
  font-size: 14px; }
  body h1 {
    font-size: 16px; }
    body h1.smaller {
      font-size: 12px; }
guillaume@ubuntu:~/$ 
```

File: [7-nested\_deeper.scss](7-nested_deeper.scss)

### 8. Margin mixin

Write a Sass file that assigns:

  - Margin left and right at `10px` to `body` tags
  - Margin left and right at `15px` to `div` tags
  - You must use a mixin

```
guillaume@ubuntu:~/$ sass 8-mixin_margins.scss | tail -n +2
body {
  margin-left: 10px;
  margin-right: 10px; }

div {
  margin-left: 15px;
  margin-right: 15px; }
guillaume@ubuntu:~/$ 
```

File: [8-mixin\_margins.scss](8-mixin_margins.scss)


### 9. Extended

Write a Sass file that assigns:

 - Font size `12px` to all tags of class `.info`
 - Text color `#00FF00` to all tags of class `.success` and extend style of the class `.info`
 - Text color `#FF0000` to all tags of class `.warning` and extend style of the class `.info`

```
guillaume@ubuntu:~/$ sass 9-extend_list.scss | tail -n +2
.info, .success, .warning {
  font-size: 12px; }

.success {
  color: #00FF00; }

.warning {
  color: #FF0000; }
guillaume@ubuntu:~/$ 
```

File: [9-extend\_list.scss](9-extend_list.scss)

### 10. Import colors 

Write a Sass file that assigns:

 - Text color `$red` from `10-colors.scss` to the class `.red`
 - Text color `$green` from `10-colors.scss` to the class `.green`
 - Text color `$blue` from `10-colors.scss` to the class `.blue`
 - You must use `@import`

```
guillaume@ubuntu:~/$ cat 10-colors.scss
/* All my colors */
$red: #FF0000;
$green: #00FF00;
$blue: #0000FF;
guillaume@ubuntu:~/$ sass 10-import_colors.scss | tail -n +3
.red {
  color: #FF0000; }

.green {
  color: #00FF00; }

.blue {
  color: #0000FF; }
guillaume@ubuntu:~/$ 
```

File: [10-import\_colors.scss](10-import_colors.scss)

### 11. For each

Write a Sass file that creates a class for each name in the list `$list-names` and assigns the background image based on the name (example below):

 - You must use `@import`
 - You must use `@each` statement

```
guillaume@ubuntu:~/$ cat 11-photos.scss 
/* All names */
$list-names: julien john sam damian;
guillaume@ubuntu:~/$ sass 11-loop_photos.scss | tail -n +3
.photo-julien {
  background: image-url("photos/julien.jpg") no-repeat; }

.photo-john {
  background: image-url("photos/john.jpg") no-repeat; }

.photo-sam {
  background: image-url("photos/sam.jpg") no-repeat; }

.photo-damian {
  background: image-url("photos/damian.jpg") no-repeat; }
guillaume@ubuntu:~/$ 
```

File: [11-loop\_photos.scss](11-loop_photos.scss)

### 12. Loop Headers

Write a Sass file that creates `H*` tags, where ‘*’ is the size of the font used.

 - _h1_ must have font size equal to _1px_, _h2_ must have font size equal to _2px_, etc.
 - You must create _H*_ tags from 1 to 5
 - You must use _@for_ statement

```
guillaume@ubuntu:~/$ sass 12-loop_header.scss | tail -n +2
h1 {
  font-size: 1px; }

h2 {
  font-size: 2px; }

h3 {
  font-size: 3px; }

h4 {
  font-size: 4px; }

h5 {
  font-size: 5px; }
guillaume@ubuntu:~/$ 
```

File: [12-loop\_header.scss](12-loop_header.scss)

### 13. Columns and operators

Write a Sass file that creates classes with different width:

    col-1 with width equals to 100%
    col-2 with width equals to 50%
    col-3 with width equals to 33.3333333333%
    col-4 with width equals to 25%
    You must create .col-* class from 1 to 4
    You must use a @for statement

```
guillaume@ubuntu:~/$ sass 100-loop_col.scss | tail -n +2
.col-1 {
  width: 100%; }

.col-2 {
  width: 50%; }

.col-3 {
  width: 33.3333333333%; }

.col-4 {
  width: 25%; }
guillaume@ubuntu:~/$ 
```

File: [100-loop\_col.scss](100-loop_col.scss)

### 14. Media query #0

Write a Sass file that assigns:

    Font size 20px to h1 tags
    Font size 14px to h1 tags, when your screen width is smaller than 320px

```
guillaume@ubuntu:~/$ sass 101-media_query.scss | tail -n +2
h1 {
  font-size: 20px; }
  @media screen and (max-width: 320px) {
    h1 {
      font-size: 14px; } }
guillaume@ubuntu:~/$ 
```

File: [101-media\_query.scss](101-media_query.scss)

### 15. Media query #1

Write a Sass file that assigns:

    Font size 20px to h1 tags
    Font size 18px to h1 tags, when your screen width is smaller than 960px
    Font size 16px to h1 tags, when your screen width is smaller than 640px
    Font size 14px to h1 tags, when your screen width is smaller than 320px
    Text color #1D1D1D to h1.small tags, when your screen width is smaller than 320px

```
guillaume@ubuntu:~/$ sass 102-media_query.scss | tail -n +2
h1 {
  font-size: 20px; }
  @media screen and (max-width: 960px) {
    h1 {
      font-size: 18px; } }
  @media screen and (max-width: 640px) {
    h1 {
      font-size: 16px; } }
  @media screen and (max-width: 320px) {
    h1 {
      font-size: 14px; }
      h1.small {
        color: #1D1D1D; } }
guillaume@ubuntu:~/$ 
```
```

File:[102-media_query.scss](102-media_query.scss)
