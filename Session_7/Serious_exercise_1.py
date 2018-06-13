# Part 1: Scrape all songs’ names and artists from the iTunes top songs and save them into a xlsx file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

top_chart_list =[]
download_list = []
# Create a connection, read & decode
url ="https://www.apple.com/itunes/charts/songs/"

html_content = urlopen(url).read().decode("utf-8")
# f = open("./itunes.html", "wb")
# f.write(html_content)
# f.close()

# Extract ROI
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())

ul = soup.find("section", "section chart-grid")
# print(ul)
li_list1 = ul.find("div", "section-content")
# print(li_list1)
li_list2 = li_list1.find("ul")
# print(li_list2)
li_list3 = li_list2.find_all("li")
# print(li_list3)

for li in li_list3:
    dictionary = {}
    h3 = li.find("h3")
    song_name = h3.string
    # print(song_name)
    h4 = li.find("h4")
    artist_name = h4.string
    # print(artist_name)
    combined_search_item = "{0} {1}".format(song_name,artist_name)
    download_list.append(combined_search_item)
    
    dictionary["artist"] = artist_name
    dictionary["song name"] = song_name
    top_chart_list.append(dictionary)


pyexcel.save_as(records =top_chart_list, dest_file_name = "top chart.xlsx")
# print(len(download_list))


# length = len(download_list)
for i in download_list:
    options = {
            "default_search": "ytsearch",
            "max_downloads": 1
        }
    dl = YoutubeDL(options)
    dl.download([i])





