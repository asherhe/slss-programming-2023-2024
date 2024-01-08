# winter holidays
# author: asher
# 2024-01-08

import random

def winter_holiday(good_or_bad: str) -> str:
  options = {
    "good": [
      "i ate breakfast :)",
      "i ate lunch :)",
      "i ate dinner :)",
      "i slept",
      "i went for a walk three times or something"
    ],
    "bad": [
      "i got sick this one time",
      "water started dripping from the ceiling somehow",
      "it was really cold but somehow there was no snow",
      "i burnt my tongue because the soup was too hot"
    ]
  }
  return random.choice(options[good_or_bad])

def main() -> None:
  for i in range(10):
    print(winter_holiday("good"))
    print(winter_holiday("bad"))

if __name__ == "__main__":
  main()