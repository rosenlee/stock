# -*- coding:utf-8 -*- 


"""

Created on 2015/10/23
@author: Rosen Lee
@group : 
@contact: rosenlove@qq.com
"""
import pandas as pd
from pandas.compat import StringIO
import numpy as np
import time
import re
import lxml.html
from lxml import etree
import json
import time
import sys
import random
#import basicData
reload(sys)
sys.setdefaultencoding('utf-8')

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
    

def getJsonText(url):
    time.sleep(random.randint(1, 13)*0.1)
    request = Request(url)
    try:
        text = urlopen(request, timeout=100).read()
        return text
    except :
        print "url Exception"
        
    
#返回结果   
"""
null({"baseinfo":{"phone":"021-36397611","address":"思南路84号底楼102室","email":"luyu@macrosilver.com","name":"上海宏银信息科技股份有限公司","shortname":"宏银信息","code":"870386","postcode":"200025","secretaries":"卢宇","industry":"软件和信息技术服务业","legalRepresentative":"王智庆","broker":"东吴证券股份有限公司","area":"上海市","listingDate":"20170111","totalStockEquity":"11000000","transferMode":"协议"},
"stamp":"2017-01-09 15:15:25.836","topTenHolders":[{"num":"1","ratio":".384","name":"王智庆","quantity":"4224000","date":"2016-09-20"},

{"num":"3","ratio":".22","name":"上海海业信息科技发展有限公司","quantity":"2420000","date":"2016-09-20"},
{"num":"4","ratio":".2","name":"上海寅辰创业投资合伙企业（有限合伙）","quantity":"2200000","date":"2016-09-20"},
{"num":"5","ratio":".1","name":"上海宏器投资合伙企业（有限合伙）","quantity":"1100000","date":"2016-09-20"},
{"num":"2","ratio":".096","name":"陈磊","quantity":"1056000","date":"2016-09-20"}],"finance":{"netAssetsYield":".0693","totalLiability":"3995928.74","profit":"969480.81","netAssets":"12809344.32","earningsPerShare":".08","income":"8131702.01","totalAssets":"16805273.06","noDistributeProfit":"1345606.61","netAssetsPerShare":"1.16","netProfit":"832401.46"}})

"""

def getCompanyName(code):
    #url = "http://www.neeq.com.cn/nq/detailcompany.html?companyCode=%s&typename=G" % (code)
    url = "http://www.neeq.com.cn//nqhqController/detailCompany.do?zqdm=%s" % (code)
    txt = getJsonText(url)
    if txt:
        return txt[5:-1]
    return txt

'''
    html = lxml.html.parse(StringIO(txt))
    res = html.xpath('//div[@class=\"list_l\"]')
    res = html.xpath('//div[@class=\"modlist\"]')
    res3 = html.xpath('//div[@class="list_l"]')
    res2 = html.xpath('//div[@class=\"modlist\"/@id=\"companymessage\"]')
    res1 = html.xpath('//div[@id="companymessage"]')
    res4 = html.xpath('//div[@id="companymessage"]/div[@class="list_l"]')
'''
    
def GetCode():  
    
    for i in range(10):  
        inListHistUrl="http://www.neeq.com.cn/nqhqController/nqhq.do?&page=%d&type=G&zqdm=&sortfield=&sorttype=&xxfcbj=&keyword=&_=1484060057056" %(i)
        print inListHistUrl
        inListHistData=getJsonText(inListHistUrl)
        print type(inListHistData)
        finalStr = inListHistData[5:-1]
        #print finalStr[0], finalStr[-1]
        jsonText = json.loads(finalStr)
        #print  jsonText
        f = open('xsbcompy.dat', 'a')
        for item  in jsonText[0]['content']:
            print item['hqzqdm'], item['hqzqjc']
            nameTxt = getCompanyName(item['hqzqdm'])            
            if nameTxt:
                js = json.loads(nameTxt)
                wStr = "\n" + item['hqzqdm'] + "," + js['baseinfo']['name'] + "," + js['baseinfo']['address'] +"," + js['baseinfo']['postcode'] +"," + js['baseinfo']['area'] 
                wStr += ","+ js['baseinfo']['listingDate'] +","+ js['baseinfo']['industry'] +","+ js['baseinfo']['phone'] + ","+ js['baseinfo']['stamp']
                f.write(wStr)
        f.close()
        
#for item in inListHistData:
#   print item[]
#print inListHistData
