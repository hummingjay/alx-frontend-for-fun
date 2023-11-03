# Forms

## Tasks

### 0. basic comment structure

To ensure we start on the same foot, use these files:
[00-article.html](00-article.html)
[00-styles.css](00-styles.css)

In your 01-article.html file

    Sibling to the <div class="post">, create a new <section> with the class post-comments
    Inside the section create an header
        In the <header> create a heading level 2 with class section-title and text: Leave a comment
        under the level 2 heading create a paragraph with text: All fields are required.
    Create a form siblings to the header
        Action: #
        Method: post

__In your__ `01-styles.css` __file__

After the `Tag list` styles, create a new comment

```
/*** FORM ***/
/* Comment section
    ============================= */
```

 - Target `post-comments` class
   - Property: `width`, Value: `80%`
   - Property: `margin`, Value: `10rem 0 0 auto`
   - Property: `padding-left`, Value: `7rem`
 - Target the `section-title` class inside the `post-comments` class
   - Property: `font-variant`, Value: `small-caps`
 - Add a new comment section

```
/* Basic form
    ============================= */
```
 - Target all `form`
   - Property: `display`, Value: `flex`
   - Property: `flex-direction`, Value: `column`
   - Property: `padding`, Value: `1rem 0`
   - Property: `margin`, Value: `0`

__Final rendering__

File: [01-article.html](01-article.html), [01-styles.css](01-styles.css)

### 1. more comment basic structure
__From__ `01-article.html`, __create__ `02-article.html`

 - In the form in the comment section
  - Create a first `fieldset` with a `legend` that has the text `Your personal information` and the class `visually-hidden`
    - In the fieldset create a first `div` with the classes `form-group` and `col-1-2`
    - Sibling to the first div, create a second `div` with the classes `form-group` and `col-1-2`
    - Sibling to the 2 divs create a third `div` with the classes `form-group` and `col-2-3`
  - Sibling to the first fieldset, create a second fieldset with a legend that has the text `Your comment` and the class `visually-hidden`
    - In the second fieldset create a first `div` with the classes `form-group` and `col-2-3`
    - Sibling to the first div create a second `div` with the classes `form-group` and `col-2-3`
    - Sibling to the 2 divs create a third `div` with the class `form-group`

__From__ `01-styles.css`, __create__ `02-styles.css`

  - Target all `fieldset` and set the following rules
    - flex display
    - direction of flex is column
    - justify the content at `flex-start`
    - no border
    - `0 0 2rem` padding

__Final rendering__ (same as previously because `<legend>` tags are hidden by default)

File: [02-article.html](02-article.html), [02-styles.css](02-styles.css)
