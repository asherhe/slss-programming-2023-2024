In Python, data can be grouped in cataegories called types.

| name | example |
| --- | --- |
| string | `"hello"` |
| list | `[1, 2, 3, 4]` |
| int | `1` `-10` `23` |
| float | `3.14`, `-2.5`, `1.0` |
| bool | `True` `False` |

An example of using these types of data:

```python
fave_food = "tempura" # string
my_age = 15 # int
```

# Type Conversion

In Python, there are some *special functions* that allow us to change the 
type of something.

```python
intro_string = "My age is " # type string
my_age = 15 # type int

# aside
"My name is" + "Slim Shady" # "My name isSlim Shady"

print(intro_string + my_age)
```

We can use the following built-in functions to convert to different types:

```python
int()
float()
str()
list()
```

We can fix the example above as follows:

```python
intro_string = "My age is"
my_age = 16

print(intro_string + str(my_age)) # "My age is16"
print(intro_string + " " + str(my_age)) # "My age is 16"
print(f"{intro_string} {my_age}") # "My age is 16"
```

