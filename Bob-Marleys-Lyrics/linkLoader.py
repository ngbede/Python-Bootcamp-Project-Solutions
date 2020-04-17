"""
run this script to generate link to each song lyric
Source: https://www.azlyrics.com/b/bobmarley.html
Note: the "Natural Mystic: The Legend Lives On" (1995) album is a compilation album, hence loading each link can lead in duplicates
except the Iron Lion Zion song. I took the liberty of cleaning up the bobslinks.txt file to contain only non duplicate songs.
113 songs contained in the file.
"""
# Libraries to be used
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
# open and close link
link = "https://www.azlyrics.com/b/bobmarley.html"
open_link = urlopen(link)
read_link = open_link.read()
open_link.close() 

# parse read_link into the soup function as html format
parsed_link = soup(read_link,"html.parser")
container = parsed_link.find_all("div",{"class":"listalbum-item"}) # contains links
site = "https://www.azlyrics.com" # main site

with open("bobslinks.txt","w") as f: # genrates link to each song and stores in a txt file i.e boboslinks.txt
   for link in container:
       f.write("%s\n" % (site + link.a["href"][2:])) # full link to each song lyric