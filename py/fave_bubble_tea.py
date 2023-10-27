# bubble tea popularity algorithm
# asher
# 2023-10-26

# ask 5 users what their favorite bubble tea place is
# prints out summary of data

# CONSTANTS
NUM_RESPONDENTS = 5 # number of respondents

like_count = {}

for _ in range(NUM_RESPONDENTS):
  # ask the user where their favorite place is
  # store it somewhere
  fave_place = input("what's your favorite bubble tea place? ").strip(".,!?").lower()
  
  # tally
  # increment a counter for each bubble tea place
  if fave_place in like_count:
    like_count[fave_place] += 1
  else:
    like_count[fave_place] = 1

# print a summary
print("\nsummary\n=======")
for place in sorted(like_count, key=like_count.get, reverse=True):
  print(f"{place}: {like_count[place]} ({like_count[place] * 100 // NUM_RESPONDENTS}%)")
