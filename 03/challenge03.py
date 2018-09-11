#!/usr/bin/env python
# @Patan
# Challenge 03: http://www.pythonchallenge.com/pc/def/equality.html
# Comments: - Based on the title of the web "re" (suggests regular expr) and
#           the hint (exactly three big bodyguads on each side)... we can guess
#           that we need to find a letter that is "surrounded" by a regular
#           expression that repeats 3 times on each side of the letter.
#           - Good help: https://www.machinelearningplus.com/python/python-regex-tutorial-examples/
#           - \W is equivalent to [^a-zA-Z_0-9]

# Imports
import re

# Open the file and get the raw string (convert it to one line string)
raw_text = "".join( open('raw_text.txt','rt').read().splitlines() )

# Apply a RegExp to retrieve the parttern
reg_exp = r'(\B[A-Za-z]+\B)\1{2}[A-Za-z]\1{3}'
#reg_exp = r'[A-Z]{3}[a-z][A-Z]{3}'
findings = re.search(reg_exp,raw_text,re.M)

# Show the results
if findings:
  print '\nFound: ', findings.group()
  print "\nHidden String:\n"
else:
  print 'Nothing found!'
