"""
crawls each individual link and stores lyrics in seperate txt files
"""
# requierd packages 
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# load links from boblinks.txt
with open("bobslinks.txt") as f:
    links = f.readlines()
# loop through links and store each lyric in a txt file
for link in links: # load link
    open_link = urlopen(link)
    read_link = open_link.read()
    open_link.close()
# pass link as html object via beautifulSoup
    parse_link = soup(read_link,"html.parser")
    lyric = parse_link.find_all("div",{"class":None})
    song_title = parse_link.find_all("b",{"class":None})
    title = song_title[1].text.strip()[1:-1] + ".txt" # song title to be used when saving the txt file
# Catch any file not found error
    try:
        with open(title,"w") as f: # store each new song lyric into its corresponding folder
            f.write("%s\n\n"%song_title[1].text.strip().upper())
            f.write("%s"%lyric[0].text.strip())  
    except FileNotFoundError:
        print(f"{title} not downloaded!")
print("Done!") # lyrics loaded succesfully!