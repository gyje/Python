import requests
import lxml
from lxml import etree#这里不知道为什么不能用import lxml然后写成lxml.etree的形式?
url="http://www.xdxfdb.com/cms/Girl/130.html"
headers={"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0"}
#cookies=[]
text=requests.get(url,headers=headers)
'''node=etree.Element(text.text)
print (node)
print (node.tag)#标签
#print (etree.tostring(node))'''
urllist=text.xpath("//li")
print (len(urllist))
'''
lxml的安装是一个大坑,而且安装好以后竟然不能用,显示AttributeError: 'Response' object has no attribute 'xpath'
而且不仅仅是这一条错误,google,baidu,stackoverflow都搜索了,没结果,放弃,直奔pyquery
'''
