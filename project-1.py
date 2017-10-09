#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/8 22:50
# @Author  : Aries
# @Site    : 
# @File    : project-1.py
# @Software: PyCharm
import urllib,urllib3
from bs4 import BeautifulSoup
import time
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
}
urls = ["https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST".format(str(i)) for i in range(30,930,30)]
url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"
def get_phone(urls,headers):
    wb_data = requests.get(urls,headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text, "lxml")
    imgs = soup.select("div.thumb.thumbLLR.soThumb > img")
    return imgs
def get_att(url,data=None):
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,"lxml")
    titles = soup.select("div.listing_title > a[target='_blank']")
    imgs = get_phone(url,headers=headers)
    cates = soup.select("div.p13n_reasoning_v2")
    for title,img,cate in zip(titles,imgs,cates):
        data = {
            "title":title.get_text(),
            "img":img.get("src"),
            "cate":list(cate.stripped_strings)
            }
        print(data)
for single_url in urls:
    get_att(single_url)

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
#         "Cookie":"TAUnique=%1%enc%3AsuluOr%2BAH81hAXokHKeJQvpe7pLCN4YdTh00SmZkzlM2jHwltRJPGQ%3D%3D; TASSK=enc%3AAPV5a%2BmyOrgTD48iSeX%2BBcvENr%2BNPQDyLq1NRzAzNnjv1pDzlvsZLd4X5s%2BrHZ681hRgKFOrJxdMnkSmnVyl6C9P31JH8gNIwCWFMzVDgZCinmKMPb6Z1da3STOBQnz%2B%2BA%3D%3D; TAPD=tripadvisor.cn; __gads=ID=9fdefb9f3f69ca0e:T=1507475572:S=ALNI_MYbstgCXiv-9JP7SIligYCaPZPjNQ; _jzqx=1.1507479328.1507479328.1.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.-; ServerPool=X; _jzqckmp=1; SecureLogin2=3.4%3AAGgNzkTiLguwyKlXvfhozPzn%2FuQ0gthJvwm3Jp6Yai0034wizeipAWvu61oO5nYsG80agpyJUNgoE1CHgbD8xnZZeG1szjNK19XLpPPRFH2uEOKugZenDH1zBvL%2FqCqBs2RiD5E8jC%2Fz4HbTGgwS2GTl4Nty9sB1VIdaWVYrQ4xT1zgZuQt9OMOIYDb%2FGI%2FChJNK0lDiYBVoP1RfXoaM2AU%3D; TAAuth3=3%3A096955d274aa3739bbbc6d67a62e6426%3AAKRE2ps%2FMiA2QqMoMpJr%2FbIHuOzC%2FcJXtavr1%2Bvkxiu%2FcanWatedEtKft3BfPIhGHtwPKeOQcyapin2KVwkEX9BCMIB9KFlQX2Dw0hAi672BDTWrKUfEm0wVcWjOIcFECzdWE5GjjSrUQQu0iDvBYsJnn17z8LSv%2FS6Az3q8mtthM%2Bqg7ws9JjL3HixqSu5rIQ%3D%3D; CommercePopunder=SuppressAll*1507563011400; BEPIN=%1%15f01c2250a%3Bbak11c.daodao.com%3A10023%3B; _smt_uid=59da4074.1e88e457; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C1%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1507475573,1507562700; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1507564300; _qzja=1.542867614.1507475573015.1507479328303.1507562700174.1507563672211.1507564300211..0.0.17.3; _qzjb=1.1507562700173.13.0.0.0; _qzjc=1; _qzjto=14.2.0; _jzqa=1.4485071671090456000.1507475573.1507479328.1507562700.3; _jzqc=1; ki_t=1507562706325%3B1507562706325%3B1507564300279%3B1%3B13; ki_r=; _jzqb=1.13.10.1507562700.1; TASession=%1%V2ID.4D141A6605D0DC0DD4D60E524F455D57*SQ.67*LP.%2FAttraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York%5C.html*PR.427%7C*LS.Saves*GR.43*TCPAR.10*TBR.42*EXEX.10*ABTR.15*PHTB.12*FS.61*CPU.97*HS.featured*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.B356E7DC6EDCC1AFD97172644FD802FF*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.60763; TATravelInfo=V2*AY.2017*AM.10*AD.22*DY.2017*DM.10*DD.23*A.2*MG.-1*HP.2*FL.3*RVL.317907_281l297390_281l1687489_281l105127_282l293916_282l8554759_282l60763_282*DSM.1507564726022*RS.1; TAUD=LA-1507562699233-1*RDD-1-2017_10_09*HDD-321957-2017_10_22.2017_10_23*LD-2026760-2017.10.22.2017.10.23*LG-2026762-2.1.F.; roybatty=TNI1625!ANkysJzVOwq7nKPFt9JUBQS5aarpj4FaTpJXVq75Q61Y3a3t1Nb1bzy2Jb8E%2FmQYjOW%2BXxym8zuEW8HdohgYHicat3ytq9tj3eaq6KFN6jwAPvJeWptaBsYQCCkbpZal%2Fq%2ForzgwcVMaL7cSLro49aK6mtO9h9dKkr0DMsLH6ovV%2C1; _ga=GA1.2.1167636251.1507475572; _gid=GA1.2.2060505184.1507475572; _gat_UA-79743238-4=1"
# }
# url_saves = "https://www.tripadvisor.cn/Saves/885504"
# wb_data = requests.get(url_saves,headers=headers)
# soup = BeautifulSoup(wb_data.text,"lxml")
# titles = soup.select("a.title")
# imgs = soup.select("div.media-left")
# cates = soup.select("div.poi_type_tages")
# print(soup,titles,imgs,cates)
# for title,img,cate in zip(titles,imgs,cates):
#     data = {
#         "title":title.get_text(),
#         "img":img.get("src"),
#         "cate":list(cate.stripped_strings)
#     }
#     print(data)
