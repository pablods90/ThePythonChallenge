#!/usr/bin/env python
# @Patan
# Challenge 08: http://www.pythonchallenge.com/pc/def/integrity.html
# Comments: None

# Imports
import bz2

# Helper
class BZ2Module:

    def __init__(self):
        self.compressor = bz2.BZ2Compressor()

    def compress_string(self, txt_to_compress):
        pass

    def decompress_string(self, txt_c):
        return repr(bz2.decompress(txt_c))


# Variables
usr = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pwd = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
all_str = [usr,pwd]

# Get our BZ2 manager
comp = BZ2Module()

for i, word in enumerate(all_str):
    print "Got new string: %s" % comp.decompress_string(word)
