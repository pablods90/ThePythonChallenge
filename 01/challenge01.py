#!/usr/bin/env python
# @Patan
# Challenge 01: http://www.pythonchallenge.com/pc/def/map.html
# Comments:     - This solution is a bit "dirty"... it can be performed more
#               efficiently using "string.maketrans()", as the same challenge
#               suggest in the solution.
#               - I resolved it using the tools I knew at that time.
#               - A cleaner solution is proposed in challenge00_enhanced.py

# Imports
import string

# Helpers
shift = lambda the_list, n : the_list[-(len(the_list)-n):] + the_list[:n]

# Variables
alphabet = list(string.ascii_lowercase)
creepy_string = (   "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq "
                    "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rf"
                    "gq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. "
                    "lmu ynnjw ml rfc spj.")

# Create shifted alphabet
shifted_alphabet = shift(alphabet,2)

# Decode string (mapping the two lists)
creepy_string = map(lambda character :  shifted_alphabet[alphabet.index(character)]
                                        if ( character in alphabet )
                                        else character,
                                        creepy_string)

# Convert the decoded list to string
creepy_string = "".join(creepy_string)

# Print decoded string
print "\nDecoded String:\n"
print creepy_string + "\n"
