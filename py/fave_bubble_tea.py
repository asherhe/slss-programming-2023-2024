# bubble tea popularity algorithm
# asher
# 2023-10-27

# ask 5 users what their favorite bubble tea place is
# prints out summary of data

# CONSTANTS
NUM_RESPONDENTS = 5 # number of respondents
BUBBLE_TEA_PLACES = ["coco", "suntea", "chatime", "bubble queen"]

# keep track of a tally for each option
like_count = {}

# repeat a number of times
for i in range(1, NUM_RESPONDENTS + 1):
  # ask the user where their favorite place is
  fave_place = input(f"user {i}, what's your favorite bubble tea place? ").strip(".,!?").lower()
  
  if fave_place not in BUBBLE_TEA_PLACES:
    fave_place = "other"

  # store it somewhere
  if fave_place in like_count:
    like_count[fave_place] += 1
  else:
    like_count[fave_place] = 1

# print a summary
print("\nsummary\n=======")
for place in sorted(like_count, key=like_count.get, reverse=True):
  # include name, count, and percent
  like_percentage = round(like_count[place] * 100 / NUM_RESPONDENTS, 2)
  print(f"{place}: {like_count[place]} ({like_percentage:.2f}%)")
