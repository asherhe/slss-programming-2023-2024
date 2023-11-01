# age in 2049
# asher
# 2023-11-01

import datetime

curr_year = datetime.date.today().year
dest_year = 2049

# ask user for age
age = int(input("how old are you? ").strip(".,!?"))

# calculate future age
print(f"in {dest_year} you will be {dest_year - curr_year + age}")
