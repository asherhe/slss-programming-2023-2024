# mcdoland's
# asher
# 2023-11-01

PRICE_BURGER = 5
PRICE_FRIES = 3
SALES_TAX = 1.14

# greet user
print("hi welcome to mcdoland's")

# ask if burger
buy_burger = input(f"would you like a burger for ${PRICE_BURGER}? (yes/no) ").lower().strip(".,!?")

# ask if fries
buy_fries = input(f"would you like a burger for ${PRICE_FRIES}? (yes/no) ").lower().strip(".,!?")

# compute total
total_price = 0
if buy_burger == "yes":
  total_price += PRICE_BURGER
if buy_fries == "yes":
  total_price += PRICE_FRIES

# tax!
total_price *= SALES_TAX

print(f"your total is ${total_price:.2f}")
