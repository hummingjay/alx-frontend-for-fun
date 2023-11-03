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
