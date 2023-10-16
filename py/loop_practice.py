# loop practice
# author: asher
# date: 2023-10-10

import time

# create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# do something for each thing in the list
# print it out in a pretty way
# e.g.
#  * hotwheels
#    ---
#  * lego
#    ---
# etc.

for item in groceries:
    print(f"# {item}\n  ---")

# print pyramid thing
for i in range(6):
    print("*" * (i + 1))

# new year countdown
for i in range(10, 0, -1):
    print(i)
    # time.sleep(1)

print("HAPPY NEW YEAR")

# implement linear search
names = []
with open("./names.txt", "r") as file:
    names = map(lambda s: s.strip("\n"), file.readlines())
search_name = "Deanna Lee"

for name in names:
    if name == search_name:
        print(f"We found {search_name}!")
        break
else:
    print(f"We didn't find {search_name}")

# print out "Mr. Ubial is pretty cool" 20 times
for _ in range(20):
    print("Mr. Ubial is pretty cool")

# count starting at 1
for i in range(100):
    print(i + 1)

# we can start somewhere else
for i in range(100, 0, -1):
    print(i)

# 1. print all even numbers in 1200 and 1500 inclusive
for i in range(1200, 1501, 2):
    print(i)

# 2. print all numbers between -150 and 0 inclusive
for i in range(-149, 0, 2):
    print(i)
