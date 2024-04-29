# Visual Cryptography Python Algorithm
from PIL import Image, ImageDraw
import os
import sys
from random import SystemRandom

random = SystemRandom()

if len(sys.argv) != 2:
    print("This script requires one argument: the image to be split.")
    exit()

infile = str(sys.argv[1])

if not os.path.isfile(infile):
    print("The specified file does not exist.")
    exit()

img = Image.open(infile)
f, e = os.path.splitext(infile)
out_filename_A = f + "_A.png"
out_filename_B = f + "_B.png"

img = img.convert('1')  # convert image to 1 bit
print("Image size: {}".format(img.size))

# prepare two empty slider images for drawing
width = img.size[0] * 2
height = img.size[1] * 2
print("{}x{}".format(width, height))

out_image_A = Image.new('1', (width, height))
out_image_B = Image.new('1', (width, height))

draw_A = ImageDraw.Draw(out_image_A)
draw_B = ImageDraw.Draw(out_image_B)

# There are 6 (4 choose 2) possible patterns
patterns = ((1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1))

# cycle through pixels
for x in range(0, int(width / 2)):
    for y in range(0, int(height / 2)):
        pixel = img.getpixel((x, y))
        pat = random.choice(patterns)

        # A will always get the pattern
        draw_A.point((x * 2, y * 2), pat[0])
        draw_A.point((x * 2 + 1, y * 2), pat[1])
        draw_A.point((x * 2, y * 2 + 1), pat[2])
        draw_A.point((x * 2 + 1, y * 2 + 1), pat[3])

        if pixel == 0:  # dark pixel so B gets the anti pattern
            draw_B.point((x * 2, y * 2), 1 - pat[0])
            draw_B.point((x * 2 + 1, y * 2), 1 - pat[1])
            draw_B.point((x * 2, y * 2 + 1), 1 - pat[2])
            draw_B.point((x * 2 + 1, y * 2 + 1), 1 - pat[3])
        else:
            draw_B.point((x * 2, y * 2), pat[0])
            draw_B.point((x * 2 + 1, y * 2), pat[1])
            draw_B.point((x * 2, y * 2 + 1), pat[2])
            draw_B.point((x * 2 + 1, y * 2 + 1), pat[3])

out_image_A.save(out_filename_A, 'PNG')
out_image_B.save(out_filename_B, 'PNG')

print("Encryption process completed successfully.")
