# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from lxml import etree
import json


def tr2list(tr):
    strtmp=etree.tostring(tr).replace("\n","")
    print (strtmp)
    tr=etree.fromstring(strtmp)
    l1 = tr.xpath("descendant::text()")
    l2 = list(l1)
    return l2


def getSensors(station,ptfCode):
    HTML = etree.HTML(station)
    datatr = HTML.xpath("//tr[@class='configs' and td='Sensors']/descendant::tr")

    tableHead = tr2list(datatr[0])
    datalist = []

    for item in datatr[1:len(datatr)]:
        valuelist = tr2list(item)
        data = {}
        for value in zip(tableHead, valuelist):
            name=value[0].replace(" ","")
            data[name] = value[1]
            data["ptfCode"]=ptfCode
        datalist.append(data)
    return datalist



f = open(r'F:\PythonLearning\resource\floatSensor' + '.html', 'w')
numbers = [2900452, 2901717, 2901702, 2901727, 2900205, 7900239, 2901723, 2901701, 2900451, 2901719, 2901217, 2902585,
           2901707, 2901736, 2901751, 2901749, 2901752, 2901703, 2901753, 2901737, 2901739, 2901708, 2901210, 2901759,
           2901748, 2901706, 2901744, 2901745, 2901718, 2901721, 2901735, 2901755, 2901725, 2901738, 2900612, 2901734,
           2901724, 2901750, 2901746, 2901757, 2901741, 2901722, 2901720, 2901754, 2901743, 2901732, 2901740, 2901758,
           5904033, 5904748, 2902054, 2902053, 2901495, 2902451, 2902052, 2902479, 2901572, 2902961, 2902050, 2903183,
           2902980, 2902407, 2902055, 2901570, 2902474, 2902057, 2902051, 2902987, 2902412, 2902654, 2902491, 2902492,
           2902990, 2903188, 2902480, 2902503, 2903187, 2902502, 2902975, 2902478, 2902518, 2903185, 2901760, 2903186,
           2902958, 5901937, 2902511, 2902692, 2901480, 2902045, 2902693, 2902691, 2901486, 2901482, 2902044, 2902698,
           2902694, 2902695, 2901481, 5904747, 2902697, 2901479, 2902037, 2902696, 2902700, 2902685, 2902962, 2902986,
           2901763, 2901764, 2902555, 5901408, 2902686, 2902549, 2901529, 2902653, 2902656, 2901524, 2902580, 2902683,
           5903429, 2901545, 2902615, 2902562, 2902688, 5901861, 2902655, 5904909, 5901690, 5903749, 2902607, 2902661]
resultlist=[]
count=0
for ptfCode in numbers:
    print count
    count+=1
    url = 'http://www.ifremer.fr/co-argoFloats/float?detail=true&ptfCode=' + str(
        ptfCode) + '&sort=PTF_CODE%3AASC&active=true&ocean=P&lang=en'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        text = response.read()
        sensor = getSensors(text,ptfCode)
        resultlist.append(sensor)

    except :
        print("error")


datajson = json.dumps(resultlist)
f.write(datajson)
f.close()
