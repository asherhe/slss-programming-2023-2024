# bubble tea popularity algorithm
# asher
# 2023-10-26

# ask 5 users what their favorite bubble tea place is
# prints out summary of data

# CONSTANTS
NUM_RESPONDENTS = 5 # number of respondents

# keep track of a tally for each option
like_count = {}

# repeat a number of times
for _ in range(NUM_RESPONDENTS):
  # ask the user where their favorite place is
  fave_place = input("what's your favorite bubble tea place? ").strip(".,!?").lower()

  # store it somewhere  
  if fave_place in like_count:
    like_count[fave_place] += 1
  else:
    like_count[fave_place] = 1

# print a summary
print("\nsummary\n=======")
for place in sorted(like_count, key=like_count.get, reverse=True):
  # include place, count, and percent
  print(f"{place}: {like_count[place]} ({like_count[place] * 100 // NUM_RESPONDENTS}%)")
