from pathlib import Path


# File Exercises
# Author: asher
# 2023-11-17

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    print(f.readline().strip())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f.readlines():
        print(line.strip())

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    data = f.readline().strip().split(",")
    print(data)

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    count = 0
    for line in f:
        data = line.strip().split(",")
        if data[1] == "Chicken Adobo":
            count += 1
    print(count)


# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    count = 0
    for line in f:
        data = line.strip().split(",")
        if data[0][0] == "A":
            count += 1
    print(count)

# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    count = 0
    for line in f:
        data = line.strip().split(",")
        if data[4] == "Guangzhou":
            count += 1
    print(count)

# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    count = 0
    for line in f:
        data = line.strip().split(",")
        if data[3][-1] in "02468":
            count += 1
    print(count)

# Problem 8*:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    food_likes = {}
    for line in f:
        food = line.strip().split(",")[1]
        if food in food_likes:
            food_likes[food] += 1
        else:
            food_likes[food] = 1
    print(max(food_likes, key=food_likes.get))
