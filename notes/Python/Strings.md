---
aliases: 
tags:
  - notes
  - python
date created: 2023/09/25 09:06:33 -07:00
date modified: 2023/10/04 14:49:53 -07:00
---
Represent a collection of characters

## F-strings

If we want to evaluate things inside of a string we can use f-strings.

To create an f-string, we put an `f` before the opening quote:

```python
a = 99
print(f"{a} bottles of beer on the wall") # "99 bottles of beer on the wall"
```

# String Methods

[[Methods]] are functions that we can use on [[objects]]

String methods allow us to modify strings.

If we want to make all the characters of a string lowercase, we can do something like this:

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOUR CHAIRS IN"
print(mr_ubial_yelling.lower())
```

The `.lower()` method takes a string and converts all uppercase characters to lowercase.
