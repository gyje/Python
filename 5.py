import requests
from bs4 import BeautifulSoup
#print (requests.get("https://www.tuicool.com"))#没有加入header和cookie所以被反爬虫检测,失败
headers={"UserAgent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'}
url="http://www.tuicool.com"
r=requests.get(url)
#print (r.url)
#print (r.text)
soup=requests(r.title)
print (soup.title)