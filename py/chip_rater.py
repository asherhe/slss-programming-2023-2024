# chip rater
# asher
# 2023-11-01

# interview people about their perception of the deliciousness of chips
# in the end, give an aggreate score

# greet user
print("please answer the following questions based on the chip you just ate.")

# create list of questions
questions = [
    "how crispy is the chip on a scale of 1 to 5? ",
    "how would you rate the taste from 1 to 5? ",
    "how would you rate the packaging from 1 to 5? "
]

final_score = 0

# ask questions
for question in questions:
  rating = int(input(question).strip(",.?!"))
  # store response
  final_score += rating

# do math
final_score /= len(questions)

# present results
print(f"this bag of chips scored a {final_score:.2f}/5")
