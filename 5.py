import requests
from bs4 import BeautifulSoup
headers={"UserAgent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'}
#cookies=dict(cookies=)
#url="http://jandan.net/ooxx/page-2008"
url="https://zhuanlan.zhihu.com/p/20858208"
r=requests.get(url,headers=headers)
print (r.url)
connect=r.text
soup=BeautifulSoup(connect,'lxml')
url = soup.select('p > img')
print (connect)
print (r.encoding)
print (r.json)
"""
看了网上的一些文档主要来源是推酷和csdn,知乎,还有一些blog,对Beautifulsoup的评价都是不如lxml,而lxml则不如pyquery,所以决定看一看lxml,BeautifulSoup终结.
