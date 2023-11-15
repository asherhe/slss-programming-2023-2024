# sfu's worst sim score
# asher
# 2023-11-14

profile = [
  "Bubble World",
  "Chef Hung",
  "Uncle Fatih's",
  "Guadalupe (MBC)",
  "Steve's Poke Bar"
]

min_sim_score = 1000000000 # basically infinity i guess
min_sim_name = ""

with open("./data.csv") as f:
  header = f.readline()
  for line in f:
    current_likes = line.split(",")
    
    current_sim_score = 0
    current_name = current_likes[1]

    for item in profile:
      if item in current_likes:
        current_sim_score += 1
    
    print(f"{current_name} score: {current_sim_score}")
    if current_sim_score < min_sim_score:
      min_sim_score = current_sim_score
      min_sim_name = current_name

print(f"\nLEAST SIMILAR PERSON:\n{min_sim_name} ({min_sim_score})")
