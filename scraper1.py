import requests
from bs4 import BeautifulSoup
import re
import urllib.request

url = "https://www.butterfliesandmoths.org/gallery?species=&family=All&subfamily=All&type=1&view=dorsal&stage=adult&sex=All&region=All"
source = requests.get(url).text
butterflies = BeautifulSoup(source, "lxml")
butterflies_properties = butterflies.find_all("div", class_="col-xs-12 col-sm-6 col-md-4 col-lg-3")
last = butterflies.find("li", class_='pager-last').a['href']
#print(last)
m = re.search('page=(.*)',last)
if m:
    lastpage=m.group(1)
    print("Number of pages: ",lastpage)

def download_images(url):

    source = requests.get(url).text

    butterflies = BeautifulSoup(source, "lxml")

    butterflies_properties = butterflies.find_all("div", class_="col-xs-12 col-sm-6 col-md-4 col-lg-3")
    butterflies_properties = butterflies.find_all("div", class_="view-content")

    #print(butterflies_properties)
    for butterfly in butterflies_properties:
        images = butterfly.find_all('img')
        #name = butterfly.find("h5",align="center").text
        #print("Downloading...    " + name)
        for img in images:
            if img.has_attr('src'):
                imgurl = img['src']
#                m = re.search('bamona_images/(.+\.jpg)',imgurl)
#                if m:
#                    imagename = m.group(1)
#                    print(imagename)
                filename = imgurl.split('/')[-1].split('?')[0]
                print(filename)
                urllib.request.urlretrieve(imgurl, filename)
print("Downloading from....:" , url)
download_images(url=url)

for i in range(1,int(lastpage)+1):
    url_i = url+"&page="+str(i)
    print(url_i)
    download_images(url=url_i)
