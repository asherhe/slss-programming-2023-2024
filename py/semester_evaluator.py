# semester evaluator

# ask for number of courses
num_courses = int(input("how many courses are you taking this semester? ").strip(".,!?"))

# get total score on courses overall
total_score = 0
for i in range(1, num_courses + 1):
  course_score = int(input(f"how would you rate course {i}? (1 to 5) ").strip(".,!?"))
  total_score += course_score

# do math
total_score /= num_courses

# tell user things
print(f"{total_score}? ", end="")
if total_score <= 1:
  print("ouch!")
elif total_score < 3:
  print("not a bad semester.")
else:
  print("glad to hear that!")

