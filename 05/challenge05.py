#!/usr/bin/env python
# @Patan / @manuk
# Challenge 05: http://www.pythonchallenge.com/pc/def/peak.html
# Comments: - "Peak hell" sounds like... Pickle!
#           - There is a file named "banner.p" in the HTML source code that looks
#           a bit strange. You just need a simple '.py' to create a pickled object
#           by yourself, open it with a text editor and check how it looks like.
#           - You may not know how a "pickled" object looks like... but for sure
#           you can tell it looks really similar to the "banner.p" object. We can
#           guess then that we have found our pickled object.
#           - WARNING: Never unpickle an object from any untrusted source. By
#           untrusted source I mean anything that was not pickled by YOU. I do not
#           trust any pickled object, not even the one on this challenge. I suggest
#           using a VM for working with this script (if possible, not running on
#           your personal computer).

# Imports
import pickle

# Helpers
decode = lambda (x,y) : x*y

# Variables
result = ""

# Get the piclked object
my_data = pickle.load( open("./banner.p","rb") )

# We discovered that the pickled object is a list of lists... It has in each
# position the character to print ("#") and the number of repetitions. We use
# the function reduce to iterate over the elements of the list, generate the
# banner and then print it!
for list in my_data:
    result += reduce( lambda a,b : a + decode(b), list , "" )
    result += '\n'

# Print the banner!
print result
