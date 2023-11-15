# similar hobbies
# asher
# 2023-11-14

# prompt for hobbies
print("please enter hobbies, separated by spaces")
p1hobbies = input("person 1: ").split(" ")
p2hobbies = input("person 2: ").split(" ")

# determine similary score
sim_score = 0
for hobby in p1hobbies:
  if hobby in p2hobbies:
    sim_score += 1

# present to user
print(f"you have {sim_score} hobbies in common!")
