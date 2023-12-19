---
aliases: 
tags: 
date created: 2023/11/24 13:49:20 -08:00
date modified: 2023/12/11 13:39:30 -08:00
---

A function is a block of code that can be reused.

We can input data into a function. This data is parameters.

We describe parameters in a docstring, which tells people what the purpose of the function is.

We use **arguments** to describe the ACTUAL data that we put into the functions.

> [!important] parameters vs arguments
> parameters = name for input
> arguments = actual data used as input

```python
def area_of_a_square(sidelength: float):
	"""Calculate and print the area of a square.
	Results are in units squared.

	Params:

	sidelength - length of one side of the square
	"""

	area = sidelength ** 2

	print(f"The area of a square with side length {sidelength} is: {area} square units.")

area_of_a_square(12.2)
```

## Functions with Return Values

If a function has a **return** keyword in the body, we can call it a **fruitful function**.

```python
def adder(x: int, y: int) -> int:
	"""Returns the sum of the given numbers"""
	sum = x + y

	return sum

adder(10, 2) # 12
```

The `return` keyword does two things in a function.

1. Stops the function
2. If there is a value after the `return` keyword, it sends the value back
   to the function call

```python
def search(l: list, item: Any) -> int:
	"""Searches through a list and returns the index.

	Params:
		l    - a list of anything
		item - thing we're looking for

	Returns:
		index in the list, -1 if not found
	"""
	counter = 0

	# search algo
	for thing in l:
		if thing == item:
			return counter
		else:
			counter += 1

	return -1
```

## Recursion

Recursion is an elegant way to repeat a pattern.

Fractals are examples of patterns that can be described recursively.

A recursive **function** must have three parts:

1. A *function*.
2. A call to itself inside of the body code block.
3. A *base case*. The base case is where the function stops calling
   itself.

### Fibonacci Sequence and Recursion

```
Fibonacci Sequence:
1  2  3
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
      x

fib(1) = 1
fib(2) = 1
fib(3) = fib(2) + fib(1)
       =      1 +      1
fib(4) = fib(3)          + fib(2)
       = fib(2) + fib(1) + fib(2)
       = 1      + 1      + fib(2)
       = 2               + 1
       = 3
fib(100) = fib(99) + fib(98)

```