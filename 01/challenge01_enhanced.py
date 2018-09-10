#!/usr/bin/env python
# @Patan
# Challenge 01: http://www.pythonchallenge.com/pc/def/map.html
# Comments:     None

# Imports
import string

# Variables
alphabet = string.ascii_lowercase
creepy_string = (   "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq "
                    "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rf"
                    "gq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. "
                    "lmu ynnjw ml rfc spj.")

# Create translation
shift = lambda the_list, n : the_list[-(len(the_list)-n):] + the_list[:n]
translation = string.maketrans(alphabet,shift(alphabet,2))

# Translate it
creepy_string = creepy_string.translate(translation)

# Print decoded string
print "\nDecoded String:\n"
print creepy_string + "\n"
