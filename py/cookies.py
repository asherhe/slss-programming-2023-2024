# cookies
# asher
# 2023-11-22

import turtle, random

# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")

def make_cookie(x: int, y: int):
  """
  creates a cookie at location (x, y)

  Params:
  x - the x-location of the centre
  y - the y-location of the centre"""

  baker_turtle.color("brown")
  baker_turtle.penup()
  baker_turtle.goto(-5 + x, -30 + y)
  baker_turtle.pendown()
  baker_turtle.circle(30)
  baker_turtle.penup()

  # Add chips
  baker_turtle.color("black")
  baker_turtle.goto(0 + x, 0 + y)
  baker_turtle.stamp()

  # Add top right, bottom right, bottom left, top left
  baker_turtle.goto(10 + x, 10 + y)
  baker_turtle.stamp()
  baker_turtle.goto(10 + x, -10 + y)
  baker_turtle.stamp()
  baker_turtle.goto(-10 + x, -10 + y)
  baker_turtle.stamp()
  baker_turtle.goto(-10 + x, 10 + y)
  baker_turtle.stamp()

# draw cookies
for _ in range(1000):
    offset_x = random.randint(-500, 501)
    offset_y = random.randint(-500, 501)

    make_cookie(offset_x, offset_y)
    
turtle.done()