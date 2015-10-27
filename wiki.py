import json
import urllib2
import sys

# Join the command line args into one string
title = " ".join(sys.argv[1:])
title = urllib2.quote(title)
try:
    json_data = json.load(urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&titles=" + title + "&prop=extracts&exintro=&explaintext=&rvprop=content&format=json"));
    try:
        pages = json_data["query"]["pages"]
        page_key = pages.keys()[0];
        text =  pages[page_key]["extract"]
        print "====="
        print text
        print "====="
    except KeyError:
        print "That page doesn't seem to exist, try changing your query!"
except urllib2.URLError:
    print "There was an error when opening the URL :( \nYou may not be connected to the interwebs!"
