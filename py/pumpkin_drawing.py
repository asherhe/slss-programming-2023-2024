# pumpkin drawing
# asher
# international spooky day

import turtle
import time
import math

# not from https://stackoverflow.com/a/41326675
def ellipse(tortoise, x_radius, y_radius, steps=60):
  down = tortoise.isdown()  # record pen state for restoration later

  if not down:
    tortoise.pendown()

  heading_radians = math.radians(tortoise.heading())
  theta_radians = -math.pi / 2
  extent_radians = 2 * math.pi
  step_radians = extent_radians / steps
  extent_radians += theta_radians
  x_center, y_start = tortoise.position()
  y_center = y_start + y_radius

  cos_heading, sin_heading = math.cos(heading_radians), math.sin(heading_radians)

  while True:
    x, y = x_center + math.cos(theta_radians) * x_radius, y_center + math.sin(theta_radians) * y_radius
    # readjust x & y to set the angle of the ellipse based on the original heading of the turtle
    x, y = x - x_center, y - y_start
    x, y = x * cos_heading - y * sin_heading, x * sin_heading + y * cos_heading
    x, y = x + x_center, y + y_start

    tortoise.setheading(tortoise.towards(x, y))  # turtle faces direction in which ellipse is drawn
    tortoise.goto(x, y)

    if theta_radians == extent_radians:
      break

    theta_radians = min(theta_radians + step_radians, extent_radians)  # don't overshoot our starting point

  tortoise.setheading(tortoise.towards(x_center, y_start))  # set correct heading for the next thing we draw

  if not down:  # restore pen state on return
    tortoise.penup()

def polygon(tortoise, x, y):
  tortoise.penup()
  tortoise.setposition(x[0], y[0])
  tortoise.pendown()
  tortoise.begin_fill()
  for i in range(len(x)):
    tortoise.setposition(x[i], y[i])
  tortoise.end_fill()
  tortoise.penup()

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.speed(0)

# stem
pumpkin.color("green")
pumpkin.pensize(25)
pumpkin.penup()
pumpkin.setposition(0, 300)
pumpkin.pendown()
pumpkin.setposition(20, 350)
pumpkin.penup()

# pumpkin
pumpkin.color("orange")
pumpkin.pensize(0)
pumpkin.setposition(0, 0)
pumpkin.begin_fill()
ellipse(pumpkin, 200, 160)
pumpkin.end_fill()

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()
carver.hideturtle()
# h
polygon(carver, [-114,-103,-83,-86,-52.5,-49,-29.4,-34,-58,-54.6,-89,-90.5], [266,184,182,217,213,178.5,164,288,265,235,239,263])
# i
polygon(carver, [5.4,4,24,26], [296,169.5,189,281])
# m
polygon(carver, [-165.5,-159,-147,-150.4,-135,-115,-111,-98,-105,-119.6,-132,-151], [164,89,94.5,137,107,135,87,70,172,156,127,156.6])
# r
polygon(carver, [-89.7,-89,-81.7,-83.4,-72.8,-62,-50.7,-66.3,-72,-67.7,-65.7,-75.3], [137,78,79.3,103.6,101.6,60.7,45.8,103.6,109,114.3,126.5,134.7])
# u
polygon(carver, [-39.6,-22.6,-22.6,-10.5,8,10,23,14.6,-4,-25.6,-34], [139.5,123.4,83.6,59.5,64,135,142,49,42,54.4,82.6])
# b
polygon(carver, [31,34,54,60.7,50.6,41,41], [103.3,46,45,62.4,79.2,73.6,95.5])
# i
polygon(carver, [63,71,82,73.6], [82,38,43,77.4,107])
# a
polygon(carver, [93,92,101,114], [79,38,47.6,46,80])
# l
polygon(carver, [121.4,130,149.4,145,120,110], [98.2,73,75.7,65,58.6,98.2])

# cool thumbs up
polygon(carver, [95.5, 89.5, 85, 72.6, 66, 63.4, 62.3, 70.3, 94.3, 123.4, 134.5, 137, 133.3, 137.8, 137.6, 132.8, 139.6, 139.2, 134, 137.6, 137.6, 128.3, 111.5, 106.3, 100.4, 104.6, 107.2, 105.7, 102.1], [260,253,230.5,213,205.7,193.6,168.4,156.7,147.7,151,156,163.7,170.2,175.6,182.5,186.3,190,198.2,201.9,206.7,214,217.2,216.5,217.8,218.7,229.3,242,252.4,258.5])

turtle.done()
