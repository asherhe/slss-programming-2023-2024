---
aliases:
  - iteration
  - loop
  - loops
  - for
tags:
  - notes
  - python
date created: 2023/10/04 14:19:25 -07:00
date modified: 2023/10/06 08:46:44 -07:00
---

# Iteration

![Loop from Giphy](https://media1.giphy.com/media/6HsjDOBPwY1eIS6kE0/giphy.gif?cid=ecf05e47u4wu0hvl9m1juhmryx7t9tw7httc7qnwe9k8shyg&ep=v1_gifs_search&rid=giphy.gif&ct=g)

We can repeat our instructions using *iteration* or *loops*.

More detailed information can be found [here](https://runestone.academy/ns/books/published/thinkcspy/Strings/TraversalandtheforLoopByItem.html).

# Iterating over a [[List]]

Say, for example, we want to repeat instructions for all items inside of a list. Python has a way that we can do this.

```python
for <item> in <list>:
	<code block>
```

We can use the rules above to iterate over a list, that is, repeat the code block for every `item` in the list.

Think of it this way. We have a list of groceries below. As you can see, Mr. Ubial has his priorities straight.

```python
groceries = ["hot wheels", "ice cream", "video games"]
```

What if you wanted to print out a formatted version of the list, something useful like putting a bullet in front of the item and putting everything on a new line.

We could do something like this:

```python
for item in groceries:
	print(f"* {item}")
	print("---")
```

Which would output this:

```console
* hotwheels
---
* ice cream
---
* video games
---
```

If we imagine that we're looping through every item in the list, the `<item>` name represents that individual item.

## Search - A Practical Example

We can implement a basic type of search algorithm using loops, one is called [linear search](https://en.wikipedia.org/wiki/Linear_search).

It goes something like this:

```pseudocodeish
for <item> in <list>:
	if <item> == <item you want to find>:
		<do something with the item>
```

Here's a practical example. Let's say that we're looking to see if Jasmine Soto is in the list. We can do this:

```python
names = ['Elizabeth Singleton', 'Raymond Mitchell', 'Steven Murphy', 'Daniel Terry', 'Glenn Fisher', 'Jasmine Soto', 'Deborah Hicks', 'Beverly Ryan', 'Jason Smith', 'Jason Washington']

for name in names:
	if name == "Jasmine Soto":
		print("We found her!")
```

## Looping $n$ times

We can iterate/looop for any number of times.

In Python, we do it a strange way:

```python
for i in range(<number of times>):
	# do something
```

e.g.

```python
# print out "Mr. Ubial is pretty cool" 20 times
for _ in range(20):
	print("Mr. Ubial is pretty cool")
```

Recall that in the other way of looping (`item in list`), `item` points to the current item in the list.

With `range`, `item` shows how many times we have looped so far

For example, we can do something like

```python
for i in range(5):
	print(i)
```

## `range()`

`range()` gives a sequence of numbers starting at 0 by default. By default it also counts up by 1. It stops before the number you provide in input

```python
range(1000) -> Sequence(0, 1, 2, ..., 99)
```

`range` also accepts starting points, stopping points, and step differences:

```python
range(<start>, <stop>, <step>)
```

**example:**

```python
range(0, 100) # sequence from 0 to 99
range(-10, 10) # sequence from -10, -9, ..., 9
```

# `break`

`break` allows us to stop a loop. Once `break` is reached, no other code afterwards will be executed.

