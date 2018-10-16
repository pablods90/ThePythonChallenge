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

# Class

class PNGHandler():

    def __init__(self, img_path):
        self.img = self._load_image(img_path)
        self.img_matrix = self._get_matrix(self.img)

    def _load_image(self, img_path):
        return Image.open(img_path)

    def _get_matrix(self, img):
        return np.array(img)

# Variables
raw_text = ''
the_string = ''

img = Image.open('oxygen.png')
arr = np.array(img)


affected_row = 45

# We hold the image in a 3d array.
# arr[row][column][R G B A]
#     95 x  629    0 1 2 3
#for affected_row in range(s, e, 1):

for i, pixel in enumerate(arr[affected_row]):

    raw_text += chr(pixel[0])

for i, c in enumerate(raw_text):
    if c is not raw_text[i-1]:
        the_string += c


print the_string


s = [105, 10, 16, 101, 103, 14, 105, 16, 121]

str = map(lambda x: chr(x),s)
print str
