#!/usr/bin/env python
# @Patan
# Challenge 02: http://www.pythonchallenge.com/pc/def/ocr.html
# Comments:     - You need to inspect the HTML and get the raw text from there.
#               - Be careful the string is UNICODE!

# Imports
import codecs
import string

# Variables
alphabet = tuple(string.ascii_letters + string.digits)

# Open the file and get the raw text (unicode!)
raw_text = codecs.open('raw_text.txt','rt',encoding='utf-8').read()

# Apply a filter
pretty_string = filter(lambda character: character in alphabet,raw_text)

# Print decoded string
print "\nHidden String:\n"
print pretty_string + "\n"
