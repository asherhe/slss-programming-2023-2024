# ball center
# asher
# 2023-01-12

from PIL import Image
import color_helper

ball_img = Image.open("./Images/Red Ball.jpeg")

center_x = 0
center_y = 0
num_red = 0

for y in range(ball_img.height):
  for x in range(ball_img.width):
    current_pixel = ball_img.getpixel((x, y))
    if color_helper.pixel_to_string(current_pixel) == "ball red":
      center_x += x
      center_y += y
      num_red += 1

print(f"({center_x / num_red}, {center_y / num_red})")
