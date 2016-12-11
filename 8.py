import requests
from lxml import etree
url="https://my.oschina.net/xxiaobian/blog/794579"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
html=requests.get(url,headers=headers)
#print (html.text)
test=etree.Element(html.text)#首先创建Element对象,和打开文件一样
#print (test)
#print (test.tag)
#print (etree.tostring(test))
hrefs=test.xpath("//*[@id="+"*"+"]/div/p[112]")
print (hrefs)

