---
aliases: 
tags:
  - notes
  - natural-language
date modified: 2023/09/20 13:26:25 -07:00
date created: 2023/09/18 08:34:08 -07:00
---

# Headers

At the top of our Python files, insert the header:

```python
# <title>
# author: asher
# date: <date>
```

# Output

We can use a function to display text and symbols to the screen.

We use the `print()` function to display output

```python
print("hello world")
```

# Input

We can grab information from the user using the `input()` function.

When we run it it does two things:

1. it waits for use to type something or nothing
2. the user presses enter/return to indicate that they are finished

# Variables

Variables allow us to store information for the time that our program is running

```python
a = 1
```

- `a`: variable name
- `=`: assignment operator
- `1`: value

> [!warning] Life lesson from Mr. Ubial
> Variable names should be as descriptive as possible

# Strings

Represent a collection of characters

## F-strings

If we want to evaluate things inside of a string we can use f-strings:

```python
a = 99
print(f"{a} bottles of beer on the wall") # "99 bottles of beer on the wall"
```