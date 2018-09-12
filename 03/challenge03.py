#!/usr/bin/env python
# @Patan
# Challenge 03: http://www.pythonchallenge.com/pc/def/equality.html
# Comments: - Based on the title of the web "re" (suggests regular expr) and
#           the hint (exactly three big bodyguads on each side)... we can guess
#           that we need to find a letter that is "surrounded" by a regular
#           expression that repeats 3 times on each side of the letter.
#           - Good help: https://www.machinelearningplus.com/python/python-regex-tutorial-examples/
#           - \w is equivalent to [^a-zA-Z_0-9].
#           - The key is "EXACTLY THREE" (not, more than three).

# Imports
import re

# Open the file and get the raw string (convert it to one line string)
raw_text = "".join( open('raw_text.txt','rt').read().splitlines() )

# Apply a RegExp to retrieve the parttern
reg_exp = r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]'
findings = re.findall(reg_exp,raw_text,re.M)

# Show the results
if findings:

    print '\nFound: ', findings, "\n"

    # Findings is a list of strings that match the rule. The rule is matched with
    # a string like this (showing the string):
    #   - [0] 1 lowercase letter
    #   - [1] 1 Capital leter
    #   - [2] 1 Capital leter
    #   - [3] 1 Capital leter
    #
    #   - [4] 1 lowercase letter (our key letter, the one we need to retrieve)
    #
    #   - [5] 1 Capital leter
    #   - [6] 1 Capital leter
    #   - [7] 1 Capital leter
    #   - [8] 1 lowercase letter
    #
    # If we keep the 4th position of each string we can get our keyword...
    #
    keyword=""
    for match in findings:
        keyword+=match[4]

    print '\nOur keyword is: ', keyword, "\n"

else:
    print 'Nothing found!'
