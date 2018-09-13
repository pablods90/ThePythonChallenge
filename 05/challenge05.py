#!/usr/bin/env python
# @Patan
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
#           using a VM for working with this script (if possible, not running on your
#           personal computer).

# Imports
import pickle
