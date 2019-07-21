"""CIS 211 Winter 2015
Project 8: Scanning HTML Documents

Part 1:
This program extracts final scores from an HTML file containing the results
of basketball games. It will use regular expressions to search for scores
in a page.

Conveniently, all the information for a game is on a single line. Program just
need to check each line in the page to see if it contains <table class="linescore">,
and if it does, use regular expressions to extract the team names and scores.

"""

from sys import argv
from re import findall  # get the data from a line. It returns the text from each
                        # group that matches a regular expression.
from urllib.request import urlopen

response = urlopen(argv[1])
doc = response.read().decode()

def regexp(doc):
    n = []
    for line in doc.split('\n'):
        if '<table class="linescore' in line:
            a = findall(r'<a href="/schools/.*?>(.*?)</a>', line)
                # The school names are enclosed in hyperlinks
                
            b = findall(r'<td class="final score">(\d+)</td>', line)
                # matches any string of 1 or more digits

            n.append(a[0]), n.append(b[0]), n.append(a[1]), n.append(b[1])

    for i in range(0, len(n), 4):
        print("{} {}, {} {}".format(n[0], n[1], n[2], n[3]))
        del n[0:4]


if __name__ == "__main__":
    regexp(doc)










