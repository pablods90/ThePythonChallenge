#!/usr/bin/env python
# @Patan
# Challenge 07: http://www.pythonchallenge.com/pc/def/oxygen.html
# Comments: - It is an RGBA image (RGB + Alpha), 4 channels (32 bytes/pixel).
#           - PNG Size: 629 x 95
#           - Black line starts at 43 ends in 51.
#

import numpy as np
from PIL import Image

img = Image.open('oxygen.png')
arr = np.array(img)

raw_text = ""

h = 95
w = 629
affected_row = 45

# We hold the image in a 3d array.
# arr[row][column][R G B A]
#     95 x  629    0 1 2 3
s = 45
e = s + 1
#for affected_row in range(s, e, 1):

for i, pixel in enumerate(arr[affected_row]):

    raw_text += chr(pixel[0])
    #arr[affected_row,i,0] = 0
    #arr[affected_row,i,1] = 0
    #arr[affected_row,i,2] = 0
the_string = ''
for i, c in enumerate(raw_text):
    if c is not raw_text[i-1]:
        the_string += c


print the_string


s = [105, 10, 16, 101, 103, 14, 105, 16, 121]

str = map(lambda x: chr(x),s)
print str
