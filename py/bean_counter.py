# bean counter
# author: asher
# 2023-01-09

# Version 0.1 ---
# Count all red pixels
# Report on the percentage of all red jellybeans
# Version 0.2 ---
# Count all the green pixels
# Report on the percantge of all green jellybeans
# Version 0.3 ---
# Count all the blue pixels
# Report on the percentage of all blue jellybeans

from PIL import Image

import color_helper

RED_PIXEL = (150, 0, 0)
GREEN_PIXEL = (0, 150, 0)
BLUE_PIXEL = (0, 0, 255)

# Calculate the percentage of pixels in some list
def calcPercentage(pixels):
    return len(pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []
green_pixels = []
blue_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x, y))

        if color_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))
        elif color_helper.pixel_to_string(current_pixel) == "jelly bean green":
            green_pixels.append((x, y))
        elif color_helper.pixel_to_string(current_pixel) == "blue":
            blue_pixels.append((x, y))

# Create a map of all "found" pixels for a respective colour
# Create a new image that is the same size as the original
original_size = (jelly_bean_img.width, jelly_bean_img.height)
blue_pixel_map = Image.new("RGB", original_size)

# For every pixel location in "found" pixel list, place a pixel on that new image
for pixel_loc in blue_pixels:
    blue_pixel_map.putpixel(pixel_loc, BLUE_PIXEL)

blue_pixel_map.save("./Images/blue_pixel_map.jpg")

blue_pixel_map.close()
jelly_bean_img.close()

# Display Report
print(f"Red Jelly Beans: {round(calcPercentage(red_pixels), 2)}%")
print(f"Green Jelly Beans: {round(calcPercentage(green_pixels), 2)}%")
print(f"Black Jelly Beans: {round(calcPercentage(blue_pixels), 2)}%")
