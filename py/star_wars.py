# star wars bot
# author: asher
# 2023-10-16

# introduce bot to the user
print("i will decide if you can join the dark side")

# ask what their favorite color is
is_red = input("is red your favorite color? ").lower().strip(".,!?")

# ask if they like capes
likes_capes = input("do you like capes? ").lower().strip(".,!?")

# decide if they are on the dark side
if is_red == "yes" and likes_capes == "yes":
    print("dark side it is!")
else:
    print("light side, i see")
