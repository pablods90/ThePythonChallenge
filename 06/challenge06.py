#!/usr/bin/env python
# @Patan
# Challenge 06: http://www.pythonchallenge.com/pc/def/channel.html
# Comments: None

# Imports
import time
import os
import re
import zipfile

# Variables
txt_file = {'nothing': '90052'}
base_dir = "channel"
all_nothings = []
comments = ""

# Get the .txt files path
base_dir = os.path.join(os.getcwd(),base_dir)

# Store the first Nothing
all_nothings.append(txt_file['nothing'])

# Now we have to play with the comments from the zipped file,
# as the last nothing suggested...
# "Collect the comments"
with zipfile.ZipFile(base_dir + '.zip','r') as the_zip:

    # Get a list of all the files
    all_the_files = the_zip.namelist()

    while True:

        # Get the current file to open
        file_to_open = txt_file['nothing'] + '.txt'

        # Get the text from the file...
        file_text = the_zip.open(file_to_open).read()

        # Parse the response to get the new nothing
        m = re.search(r'Next nothing is ([0-9]+)',file_text,re.U)

        # If found a new one... update and keep going.
        # Note:
        #       We are taking only the capture group 1... which is our number.
        if m is not None:
            txt_file['nothing'] = m.group(1)

        # If we do not find a match... we assume that we reached the end of
        # the chain.
        else:
            print "\nEnd of the chain!"
            print "\nThe last file is: %s\n" % file_to_open
            print file_text
            break

        # Show the progress...
        print "\nSearching in file: \t\t%s" % file_to_open
        print "Got new nothing: \t%s" % txt_file['nothing']

        # Nothing loop detector (just in case)...
        if txt_file['nothing'] not in all_nothings:
            all_nothings.append(txt_file['nothing'])
        else:
            print "Repeated nothing! You are in a loop..."
            exit(-1)

        # Store the comment of the current file
        comments += the_zip.getinfo(file_to_open).comment

# Print the final string
print comments
