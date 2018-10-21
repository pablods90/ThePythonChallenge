#!/usr/bin/env python
# @Patan
# Challenge 07: http://www.pythonchallenge.com/pc/def/oxygen.html
# Comments: - It is an RGBA image (RGB + Alpha), 4 channels (32 bytes/pixel).
#           - PNG Size: 629 x 95
#           - Black line starts at row 43 and ends at row 51.
#           - You need to figure out that each different color in the 'black'
#           line in the middle of the photo, represents ASCII values of a secret
#           String.
#           - We can pick any row between 43 and 51 to get our string.

# Imports
import numpy as np
from PIL import Image

# Helper Class
class PNGHandler():

    def __init__(self, img_path):
        self.img = self._load_image(img_path)
        self.img_matrix = self._get_matrix(self.img)

    def _load_image(self, img_path):
        return Image.open(img_path)

    def _get_matrix(self, img):
        return np.array(img)

    def get_pixel(self, row, column):
        return self.img_matrix[row][column]

    def get_row(self, row):
        return self.img_matrix[row]

    def get_width(self):
        return len(self.img_matrix[0])

    def get_height(self):
        return len(self.img_matrix)

# Variables
raw_text = ''
step = 7
slected_row = 45

# Create the PNGHandler
the_png = PNGHandler('oxygen.png')

# Print info
w = the_png.get_width()
h = the_png.get_height()
print "Working with image %dx%d" % (w,h)

# - We hold the image in a 3d array.
# arr[row][column][R G B A]
#     95 x  629    0 1 2 3
# - We always use the positon 0 of the pixel, as the three values
# are the same for our greyscale pixels (RGBA).
# - As the grayscale blocks are 7 pixels width, our step in the iteration
# is 7.
for i in range(0,w,step):
    raw_text += chr(the_png.get_pixel(slected_row,i)[0])

# Print the string
print "\nHidden text found:\n%s \n" % raw_text

# Now we try to figure out the decoded text...
s = [105, 110, 116, 101, 103, 114, 105, 116, 121]
str = map(lambda x: chr(x),s)

# Show the string
print "\nOur secret string is: %s.\n" % ''.join(str)
