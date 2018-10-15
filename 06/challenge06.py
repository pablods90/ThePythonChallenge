#!/usr/bin/env python
# @Patan
# Challenge 06: http://www.pythonchallenge.com/pc/def/channel.html
# Comments: This is one of the trickest challenges... I spent a lot of time
#           playing with Python ZIP method, trying to combine lists from the
#           previous pickled object. I really lost a lot of time... until while
#           I was running out of ideas I tried replacing the ".html" for a ".zip"
#           in the URL. Got it! Yo download a .zip file full of nothnigs...

# Imports
import time
import os
import re
import zipfile

# Variables
txt_file = {'nothing': '90052'}
zip_name = "channel.zip"
all_nothings = []
comments = ""

# Get the zip file path
zip_name = os.path.join(os.getcwd(),zip_name)

# Store the first Nothing
all_nothings.append(txt_file['nothing'])

# Now we have to go through all the files, get the name for
# the next one... and go on until we reach the last file.
with zipfile.ZipFile(zip_name,'r') as the_zip:

    while True:

        # Get the current file to open
        file_to_open = txt_file['nothing'] + '.txt'

        # Get the text from the file...
        file_text = the_zip.open(file_to_open).read()

        # Parse the text to get the new nothing
        m = re.search(r'Next nothing is ([0-9]+)',file_text,re.U)

        # If found a new one... update and keep going.
        # Note:
        #       We are taking only the capture group 1... which is our number.
        if m is not None:
            txt_file['nothing'] = m.group(1)

            # Store the comment of the current file
            comments += the_zip.getinfo(file_to_open).comment

            # Show the progress...
            print "\nSearching in file: \t\t%s" % file_to_open
            print "Got new nothing: \t%s" % txt_file['nothing']

            # Nothing loop detector (just in case)...
            if txt_file['nothing'] not in all_nothings:
                all_nothings.append(txt_file['nothing'])
            else:
                print "Repeated nothing! You are in a loop..."
                exit(-1)

        # If we do not find a match... we assume that we reached the end of
        # the chain.
        else:
            print "\nEnd of the chain!"
            print "\nThe last file is: %s\n" % file_to_open
            print "The found text is: %s" % file_text
            break

# Print the final string
print "\nThe ASCII art is:\n\n%s" % comments

# This leads us to we the URL: http://www.pythonchallenge.com/pc/def/hockey.html
# Each letter from the word HOCKEY, is made up entirley with one letter. That
# leads us to the word "OXYGEN".
