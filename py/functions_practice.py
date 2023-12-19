# functions practice
# asher
# 2023-11-27

# question 1

def stars(length: int) -> str:
  """
  constructs a string of stars of length `length`
  """
  return "*" * length

print(stars(1)) # *
print(stars(3)) # ***
print(stars(10)) # **********

# question 2

def biggest_of_three(a: float, b: float, c: float) -> float:
  """
  determines the largest of `a`, `b`, and `c`
  """
  if a > b and a > c:
    return a
  elif b > c:
    return b
  else:
    return c

print(biggest_of_three(1, 2, 3))
print(biggest_of_three(1, 3, 2))
print(biggest_of_three(3, 2, 1))
print(biggest_of_three(3, 3, 5))

# question 3

def pyramid(height: int):
  """
  constructs an ascii art pyramid of size `height`
  """
  for i in range(1, height + 1):
    print(stars(i))

pyramid(1)
print()
pyramid(5)
print()

# question 4

def pyramid_mirror(height: int):
  """
  similar to `pyramid()`, but right-aligned
  """
  for i in range(1, height + 1):
    print(" " * (height - i) + stars(i))

pyramid_mirror(1)
print()
pyramid_mirror(5)
