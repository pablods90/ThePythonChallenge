#!/usr/bin/env python
# @Patan
# Challenge 03: http://www.pythonchallenge.com/pc/def/equality.html
# Comments: - Based on the title of the web "re" (suggests regular expr) and
#           the hint (exactly three big bodyguads on each side)... we can guess
#           that we need to find a letter that is "surrounded" by a regular
#           expression that repeats 3 times on each side of the letter.

# Imports
import re

# Open the file and get the raw text
raw_text = open('raw_text.txt','rt').read()

# Apply a filter
reg_exp = r'(.*){3}\w(.*){3}'
hidden_letter = re.search(reg_exp,raw_text,re.M|re.I)

# Print hidden letter
print "\nHidden String:\n"
print hidden_letter.group() + "\n"
