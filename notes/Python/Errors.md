---
aliases:
  - error
  - errors
  - syntax error
  - syntax errors
  - semantic error
  - semantic errors
tags: 
  - notes
  - python
date created: 2023/10/04 14:21:40 -07:00
date modified: 2023/10/06 08:50:16 -07:00
---

# Syntax Errors

These types of errors are ones where you run your code and something breaks.

Syntax errors are relatively easy to fix.

Syntax errors happen when we don't follow the rules completely.

Some examples are when we forget a closing `"`. Or if we're missing a closing parenthesis.

# Semantic Errors

Semantic errors are much more challenging (in the great Mr. Ubial's opinion) to squash.

Semantic errors are when your code doesn't "mean" what you actually mean.

```python
user_response = input("Do you like to eat food? ")

if user_response == "yes":
	print("You passed the human test.")
else:
	print("You must be some sort of robot.")
```

The problem with the above code is subtle. What I mean is that if the user answers with ANYTHING affirmative, the code should go into the ``"yes"`` block. However, if the user writes with uppercase letters, the program will go into the `"no"` block.

One way to solve this problem is to use [[Strings#String Methods|string methods]]. We can use `.lower()` to catch all permutations of capital letters.

```python
user_response = input("Do you like to eat food? ")

if user_response.lower() == "yes":
	print("You passed the human test.")
else:
	print("You must be some sort of robot.")
```
