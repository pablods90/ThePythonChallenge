#!/usr/bin/env python
# @Patan
# Challenge 04: http://www.pythonchallenge.com/pc/def/linkedlist.php
# Comments: - In the web page source there is a comment that suggests using
#           the urlib.
#           - There are a lot of 'nothings'!! Be patient... the script may take
#           a while to complete.

# Imports
import requests
import time
import re

# Variables
parameters = {'nothing': '12345'}
base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
url = 'http://www.pythonchallenge.com/pc/def/'

# We do it at least 400 times (as the hint suggests...)
# Notes:
#       We will follow the chain, staring from the first nothing (12345)
#       and then parsing each retrieved page to get the next nothing...
for i in range(400):

    # Get the web page
    web_page = requests.get(base_url,params=parameters)

    # Parse the response to get the new nothing
    new_nothing = re.search(r'[0-9]+', web_page.text, re.U)

    # If found a new one... update and keep going. If not... we are done!
    if new_nothing is not None:
        parameters['nothing'] = new_nothing.group()

    elif parameters['nothing'] == '16044':
        # Get rid of tricky Nothings... by checking some special ones.
        parameters['nothing'] = str(int('16044')/2)

    else:
        print "\nEnd of the chain!"
        print "\nThe last page is: ", web_page.url, "\n"
        print web_page.text
        print "The url is: "
        exit()

    # Show the progress
    print "\nSearching URL: \t\t", web_page.url
    print "Got new nothing: \t", parameters['nothing']
    #time.sleep(1)
