# olypmpic judging
# asher
# 2023-11-01

NUM_JUDGES = 5

total_score = 0

# get scores
for i in range(1, NUM_JUDGES + 1):
  score = float(input(f"judge {i}: ").strip(",!?"))
  # add to tally
  total_score += score

# do math
total_score /= NUM_JUDGES

# print result
print(f"your olympic score is {total_score}")