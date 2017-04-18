# -*- coding:utf-8 -*-
from lxml import etree
import json
import time

inpath = r"F:\PythonLearning\resource\float1.html"
inf = open(inpath, 'r')
text = inf.read()
rawData = etree.fromstring(text)
trs = rawData.xpath("/data/tr")

datalist = []
i = 0

while i < len(trs):
    datadict = {}
    td = trs[i].xpath("child::td")
    datadict[td[0].text] = str(td[1].text).replace("\n", "")
    i += 1

    td = trs[i].xpath("child::td")
    datadict[td[0].text] = str(td[1].text)
    datadict[td[0].text + '1'] = str(td[1].text).replace(" ", "-")  # alias name
    i += 1

    td = trs[i].xpath("child::td")
    datadict[td[0].text] = str(td[1].text).replace("\n", "")
    i += 1

    td = trs[i].xpath("child::td")
    datadict[td[0].text] = td[1].text
    i += 1

    td = trs[i].xpath("child::td")
    datadict[td[0].text] = str(td[1].text).replace("\n", "")
    i += 1

    td = trs[i].xpath("child::td")
    datadict[td[0].text] = str(td[1].text).replace("\n", "")
    i += 1

    td = trs[i].xpath("child::td")
    a = str(td[1].text)
    timeArray = time.strptime(a, "%d/%m/%Y %H:%M:%S")
    a = time.strftime("%Y-%m-%dT%H:%M:%S.0Z", timeArray)
    datadict[td[0].text] = a
    i += 1

    datalist.append(datadict)

datajson = json.dumps(datalist)

outpath = r"F:\PythonLearning\resource\data.txt"
fout = open(outpath, 'w')
fout.write(datajson)
fout.close()
