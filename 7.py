from pyquery import PyQuery as pq
#doc=pq("<html><a href="https://www.douban.com"></a></html>")
doc2=pq("http://www.xdxfdb.com/cms/Girl/130.html")
print (doc2.html())
print (type(doc2))
a=doc2("jpg")
print (type(a))
print (a.text)