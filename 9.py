import requests
from bs4 import BeautifulSoup
url="http://jandan.net/ooxx"
headers={"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
a=requests.get(url,headers=headers)
b=BeautifulSoup(a.text,"lxml")

'''def image_download(img_url):
    a=requests.get(img_url)
    with open("%s.jpg"%str(range(0,1000)),"wb") as fp:
        fp.write(a.content)

fob=open("9.txt")
for img_url in fob.readline():
    #image_download(img_url)
    print (img_url)'''

fob=open("9.txt","w+")
for i in b.find_all("img"):
    for m in i.get("src"):
        fob.write(m)
       
