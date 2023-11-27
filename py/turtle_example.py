# turtle example
# asher
# 2023-11-21

import turtle

FORWARD_MAGNITUDE = 50

# create a turtle that moves around the screen

# make a turtle object
mike = turtle.Turtle()

# get some input from the user
print("To give commands, type:\nF - go forward\nL - turn left\nR - turn right\nQ - quit")

done = False

while not done:
    command = input("where should i go? ").strip(".,!?").lower()
    if command == "f":
        mike.forward(FORWARD_MAGNITUDE)
    elif command == "l":
        mike.left(90)
    elif command == "r":
        mike.right(90)
    elif command == "q":
        done = True
