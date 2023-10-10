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
    time.sleep(1)

print("HAPPY NEW YEAR")
