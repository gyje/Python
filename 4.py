#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like Gecko)Chrome/50.0.0000.101 Safari/537.36"
}
url=requests.get("https://my.oschina.net/xxiaobian/blog/790934")
data=BeautifulSoup(url.text)
for index, each in enumerate(data.select('#comments img')):
        with open('{}.jpg'.format(index), 'wb') as jpg:
                jpg.write(requests.get(each.attrs['src'], stream=True).content)