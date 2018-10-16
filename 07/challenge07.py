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

    def filter_duplicates(self, raw_text):
        the_string = ''
        for i, c in enumerate(raw_text):
            if c is not raw_text[i-1]:
                the_string += c

        return the_string

# Variables
raw_text = ''
slected_row = 45

# Create the PNGHandler
the_png = PNGHandler('oxygen.png')

# We hold the image in a 3d array.
# arr[row][column][R G B A]
#     95 x  629    0 1 2 3
# We always use the positon 0 of the pixel, as the three values
# are the same for our greyscale pixels (RGBA).
for i, pixel in enumerate(the_png.get_row(slected_row)):
    raw_text += chr(pixel[0])

# Filter duplicated characters & print the string
print "\nHidden text found:\n%s \n" % the_png.filter_duplicates(raw_text)

# Now we try to figure out the decoded text...
s = [105, 10, 16, 101, 103, 14, 105, 16, 121]

str = map(lambda x: chr(x),s)

s=''

for c in str:
    s+=c
print '\n'
print str
print s
