#!/usr/bin/env python
import string

# Variables
abcd = list(string.ascii_lowercase)
my_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# Decode string
my_string = map(lambda letra : chr(ord(letra) + 2), my_string)

# Convert the decoded list to string
my_string = "".join(my_string)

print my_string
