#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 23:20
# @Author  : Aries
# @Site    : 
# @File    : netdatatodatabase.py
# @Software: PyCharm
import pymongo

client = pymongo.MongoClient("localhost",27017)
walden = client["walden"]
sheet_line = walden["sheet_lines"]

# path = "C:\\Users\\roy\\Desktop\\walden.txt"
# with open(path,"r") as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         dic = {
#             "index":index,
#             "line":line.strip(),
#             "words":len(line.split())
#         }
#         sheet_line.insert_one(dic)
for item in sheet_line.find({"words":{"$lt":4}}):
    print(item)

