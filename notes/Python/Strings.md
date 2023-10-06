---
aliases: 
  - string
  - strings
tags:
  - notes
  - python
date created: 2023/09/25 09:06:33 -07:00
date modified: 2023/10/06 08:50:37 -07:00
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

[[Methods]] are functions that we can use on [[Objects|objects]]

String methods allow us to modify strings.

## `.lower()`

If we want to make all the characters of a string lowercase, we can do something like this:

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOUR CHAIRS IN"
print(mr_ubial_yelling.lower())
```

The `.lower()` method takes a string and converts all uppercase characters to lowercase.

## `.upper()`

The `.upper()` method uppercases all the letters

## `.strip(chars)`

The `.strip()` method **removes** characters from both the beginning and the end of the string.

```python
user_feeling = input("How are you feeling today? ")

# "good!", "good.", "Good!", "GOOOOOD!!!!!"
if user_feeling.lower().strip(".,!") == "good":
	print("That's great!")
```

## `.split(str)`

The `.split()` method splits a string into a [[Lists|list]], separating the string based on the characters you give it.

```python
grocery_str = "eggs milk cheese hotwheels"

grocery_list = grocery_str.split(" ");
```

---

We can use string methods to help solve [[Errors#Semantic Errors|semantic errors]]
