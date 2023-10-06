# food suggestion bot
# asher
# 2023-10-06

# a bot that asks the user what their favorite foood is.
# based on that food, it will classify the type/gentre/cuisine of the food,
# then give a restaraunt suggestion

import time
import random

# introduce the bot to the user
# ask the user what their favorite food is
print("hello, i am here to suggest you a restaraunt.")
time.sleep(0.5)
fave_food = (
    input("to help me suggest a restaraunt, tell me what your favorite food is: ")
    .lower()
    .strip(".,!?")
)

# list of cuisines
italian_food = ["pasta", "pizza", "canneloni", "tiramisu"]
fast_food = ["burgers", "fries", "chicken nuggets"]

# if they answer with italian food,
# suggest an italian restaraunt
if fave_food in italian_food:
    print("i see that you like italian food.")
    time.sleep(1)
    print("i suggest broli kitchen")
    time.sleep(0.5)
    print("here is their address:")
    time.sleep(0.5)
    print("186-8180 no 2 rd, richmond, bc")
elif fave_food in fast_food:
    print("i see that you like fast food.")
    time.sleep(1)
    print("i suggest mcdonalds")
    time.sleep(0.5)
    print("here is their address:")
    time.sleep(0.5)
    print("8140 no 2 rd, richmond, bc")
else:
    print("sorry, i'm not sure what kind of food that is.")
    time.sleep(0.5)
    print("i can't make a suggestion")
