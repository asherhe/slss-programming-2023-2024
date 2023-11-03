# world traveller
# asher
# 2023-11-03

# ask for user name
name = input("what's your name? ")
print(f"hello, {name}, it's nice to meet you!")

# list of continents
CONTINENTS = [
  "north america",
  "south america",
  "europe",
  "africa",
  "asia",
  "australia",
  "antarctica"
]

continents_visited = 0
for continent in CONTINENTS:
  been_there = input(f"have you been to {continent}? ").strip(".,!?").lower()
  if been_there == "yes":
    continents_visited += 1

print(f"i see, you've been to {continents_visited}/{len(CONTINENTS)} continents")
