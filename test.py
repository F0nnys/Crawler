#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 0:42
# @Author  : Aries
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import time
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
}
urls = ["https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST".format(str(i)) for i in range(30,930,30)]
for i in urls:
    wb_data = requests.get(i,headers=headers)
    soup = BeautifulSoup(wb_data.text, "lxml")
    imgs = soup.select("div.thumb.thumbLLR.soThumb > img")
    for k in imgs:
        print(k.get("src"))
