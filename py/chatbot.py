# chatbot
# author: asher
# date: 2023-09-20

import random
import time


def typewriter(msg):
    for c in msg:
        print(c, end="")
        if c in ".!?":
            time.sleep(0.2)
        elif c == ",":
            time.sleep(0.1)
        else:
            time.sleep(0.05)


# greet the user
# get the user's name and store it in a variable
typewriter("hi! i'm a crude chatbot.\n")
time.sleep(0.5)
typewriter("what's your name? ")
name = input()
time.sleep(1)

# respond with user's name
typewriter(f"it's good to meet you, {name}!\n")
time.sleep(1.5)

# ask the user what their favorite food is
typewriter("what's your favorite food? ")
food = input()
time.sleep(1)

# make a NOT REPETITIVE comment about their food
# create list of possible responses
food_responses = [
    f"yum, {food}!\n",
    f"{food} is delicious!\n",
    f"ew, {food} is disgusting!\n",
    f"hmm, i've never had {food} before.\n",
]
# choose a random one
# print that one
typewriter(random.choice(food_responses))
