# chatbot
# author: asher
# date: 2023-09-20

import random

# greet the user
# get the user's name and store it in a variable
name = input("hi! i'm a bot. what's your name? ")
# respond with user's name
print(f"it's good to meet you {name}!")
# ask the user what their favorite food is
food = input("what's your favorite food? ")
# make a NOT REPETITIVE comment about their food
# create list of possible responses
food_responses = [
    f"yum, {food}!",
    f"{food} is delicious!",
    f"ew, {food} is disgusting",
    f"i've never had {food} before",
]
# choose a random one
# print that one
print(random.choice(food_responses))
