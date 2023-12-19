# binarized image
# asher
# 2023-12-19

import color_helper

from PIL import Image

with Image.open("./images/best_pizza.jpg") as im:
  image_height = im.height
  image_width = im.width

  for y in range(image_height):
    for x in range(image_width):
      pixel = im.getpixel((x, y))

      # check if pixel is white
      if color_helper.is_light(pixel):
        im.putpixel((x, y), (255, 255, 255))
      else:
        im.putpixel((x, y), (0, 0, 0))

  # save the image
  im.save("./Images/output.jpg")
