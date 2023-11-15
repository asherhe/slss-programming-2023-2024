# parental bot
# asher
# 2023-11-15

# list of questions to ask
questions = [
  "did you eat? ",
  "did you study? ",
  "did you do your laundry? ",
  "did you call your grandma? "
]

# ask each question and increment score if necessary
score = 0
for question in questions:
  answer = input(question).lower().strip(".,!?")
  if answer == "yes":
    score += 1

# reply depending on score
if score == 0:
  print("i'm coming over.")
elif score <= 2:
  print("ok.")
else:
  print("good!")
