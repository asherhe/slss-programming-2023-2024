# similarity score
# asher
# 2023-11-10

# calculate simularity score between two people

# create two lists that represent movies people like
ubials_favourite_movies = [
    "The Matrix",
    "Avengers: Infinity War",
    "The Empire Strikes Back",
    "Infernal Affairs",
    "Rogue One"
]
bens_favourite_movies = [
    "Thomas and Friends Big World Big Adventure",
    "Infernal Affairs",
    "Rogue One",
    "Spider-man: Into the Spider-verse",
    "Guardians of the Galaxy: Volume 3"
]

# initialize similarity score
similarity_score = 0

# for each item in the first list
for movie in ubials_favourite_movies:
  # if that item is in the second list
  if movie in bens_favourite_movies:
    # increment similarity score
    similarity_score += 1

# display results
print(f"similarity score: {similarity_score}")
