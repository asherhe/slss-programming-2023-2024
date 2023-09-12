---
aliases: 
tags:
  - markdown 
date created: 2023/09/08 08:45:29 -07:00
date modified: 2023/09/11 09:18:47 -07:00
---

# Headings

Use `#` to create headings

```markdown
# heading 1
## heading 2
### heading 3
#### heading 4
##### heading 5
###### heading 6
```

# heading 1

## heading 2

### heading 3

#### heading 4

##### heading 5

###### heading 6

# Text Style

## Bold and Italic

Use asterisks `*` to modify text style:

- *italic* `*italic*`
- **bold** `**bold**`
- ***bold and italic*** `***bold and italic***`

> [!sidenote]
> The backslash character `\` can be used to escape special characters such as `*` and `#`

## Strikethrough

Use `~` to strikethrough:

~~strikethrough~~ `~~strikethrough~~`

# Links

- external link: [Obsidian](https://obsidian.md) `[Obsidian](https://obsidian.md)`

> [!exercise] Exercise (with ChatGPT)
> - Ask ChatGPT to create markdown code that is linked to two websites of your choice.
> - If you don't have ChatGPT, create two links to websites of your choice in the space below:

- [google](http://google.com)
- [chatgpt](https://chat.openai.com)

# Images

## Method 1

Similar to [[#Links]] but insert a `!` in front

```
![pineapple](https://upload.wikimedia.org/wikipedia/commons/6/67/Abacaxi_%28Ananas_comosus%29_2014-07-14_20-40.jpg)
```

![pineapple](https://upload.wikimedia.org/wikipedia/commons/6/67/Abacaxi_%28Ananas_comosus%29_2014-07-14_20-40.jpg)

## Method 2

```
![pineapple][pineapple]

[pineapple]: https://upload.wikimedia.org/wikipedia/commons/6/67/Abacaxi_%28Ananas_comosus%29_2014-07-14_20-40.jpg
```

> [!warning]
> This method does not work in Obsidian!

# Blockquotes

Used to emphasize a block of text. Typically used for quotes.

Prepend a caret (`>`) to create a blockquote

```
> blockquote
```

> blockquote

Blockquotes can contain multiple lines.

```
> line 1
> line 2
```

> line 1
> line 2

# Lists

## Unordered Lists

- prepend `-` to lines to create an unordered list
- i.e. `- bullet point`

Unordered lists can also have hierarchy:

```
- a
  - aa
  - ab
    - abc
  - ac
- b
  - ba
  - bb
```

- a
  - aa
  - ab
    - abc
  - ac
- b
  - ba
  - bb

## Ordered Lists

```
1. one
2. two
3. three
```

1. one
2. two
3. three

## Tables

We can organize information in tables in markdown.

Use `|` to separate columns
Use `-` to indicate the line underneath the header row:

```
| column 1 | column 2 | column 3 |
| -------- | -------- | -------- |
| 1        | a        | aa       |
| 2        | b        | asd      |
| 3        | c        | sdfsx    |
| 4        | d        | sdfxc    |
```

| column 1 | column 2 | column 3 |
| -------- | -------- | -------- |
| 1        | a        | aa       |
| 2        | b        | asd      |
| 3        | c        | sdfsx    |
| 4        | d        | sdfxc    |

# Paragraphs

Paragraphs are separated by a blank line:

```
paragraph 1

paragraph 2
```

> paragraph 1
> 
> paragraph 2

Two lines can be joined into one paragraph by appending two spaces (not necessary in obsidian)
