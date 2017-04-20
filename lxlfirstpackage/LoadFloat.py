# -*- coding:utf-8 -*-
import urllib
import urllib2
from lxml import etree
import time
import processsos

class SensorError(Exception):
  pass

def tr2list(tr):
    strtmp = etree.tostring(tr).replace("\n", "").replace("&", "")
    # print (strtmp)
    tr = etree.fromstring(strtmp)
    l1 = tr.xpath("descendant::text()")
    l2 = list(l1)
    return l2


def delRepeat(liebiao):
    for x in liebiao:
        while liebiao.count(x) > 1:
            del liebiao[liebiao.index(x)]
    return liebiao


def getStationCode(html):
    path = '/html/body/div[2]/table/tr[1]/td[2]'
    return html.xpath(path)[0].text.replace('\n', '').replace('&', '')


def getStationName(html):
    path = '/html/body/div[2]/table/tr[2]/td[2]'
    return html.xpath(path)[0].text.replace('\n', '').replace('&', '')


def getDescription(html):
    path = '/html/body/div[2]/table/tr[3]/td[2]'
    return html.xpath(path)[0].text.replace('\n', '').replace('&', '')


def getProject(html):
    path = '/html/body/div[2]/table/tr[4]/td[2]'
    return html.xpath(path)[0].text.replace('\n', '').replace('&', '')


def getInstitution(html):
    path = '/html/body/div[2]/table/tr[5]/td[2]'
    return html.xpath(path)[0].text.replace('\n', '').replace('&', '')


def getTime(html):
    path = '/html/body/div[2]/table/tr[10]/td[2]'
    a = html.xpath(path)[0].text.replace('\n', '').replace('&', '')
    timeArray = time.strptime(a, "%d/%m/%Y %H:%M:%S")
    return time.strftime("%Y-%m-%dT%H:%M:%S.0Z", timeArray)


def getSensorNamelist(html):
    path = "//tr[@class='configs' and td='Sensors']/descendant::tr"
    datatr = html.xpath(path)
    name1=str(datatr[1].xpath("child::td[3]")[0].text).replace(' ','-')
    SerialNumber1 = str(datatr[1].xpath("child::td[4]")[0].text)
    # loadsensorNamelist=[sensorName+serialnum,]
    loadsensorNamelist = []

    for item in datatr[1:len(datatr)]:
        item.xpath("child::td")
        name = str(item.xpath("child::td[3]")[0].text or name1)
        # if name=="": name=name1
        name=name.replace(' ','-')
        SerialNumber = str(item.xpath("child::td[4]")[0].text or SerialNumber1)
        # if SerialNumber=="":SerialNumber=SerialNumber1
        loadsensorNamelist.append(name + '-' + SerialNumber)
    loadsensorNamelist = delRepeat(loadsensorNamelist)
    return loadsensorNamelist

def getSensors(html):
    path = "//tr[@class='configs' and td='Sensors']/descendant::tr"
    datatr = html.xpath(path)
    maker1=str(datatr[1].xpath("child::td[2]")[0].text)
    name1 = str(datatr[1].xpath("child::td[3]")[0].text).replace(' ', '-')
    SerialNumber1 = str(datatr[1].xpath("child::td[4]")[0].text)

    # 获取序列号,并去重
    nameandNumberlist = []
    for item in datatr[1:len(datatr)]:
        name = str(item.xpath("child::td[3]")[0].text or name1)
        # if name == "": name = name1
        name = name.replace(' ', '-')
        SerialNumber = str(item.xpath("child::td[4]")[0].text or SerialNumber1)
        # if SerialNumber == "": SerialNumber = SerialNumber1
        nameandNumberlist.append((name,SerialNumber))
    nameandNumberlist = delRepeat(nameandNumberlist)

    #根据序列号,查找传感器
    sensorslist=[]
    for sensorname,sensornum in nameandNumberlist:
        inputlist=[]
        for item in datatr[1:len(datatr)]:
            valuelist = tr2list(item)
            if len(valuelist) < 4: continue

            maker = str(item.xpath("child::td[2]")[0].text or maker1).replace(' ','')
            # if maker=="": maker=maker1
            SerialNumber = str(item.xpath("child::td[4]")[0].text or SerialNumber1)
            # if SerialNumber == "": SerialNumber = SerialNumber1
            unit=str(item.xpath("child::td[1]")[0].text).replace(' ','')
            Accuracy=str(item.xpath("child::td[6]")[0].text or '00')
            # if Accuracy == "":  Accuracy='0'
            Resolution=str(item.xpath("child::td[7]")[0].text or '00')
            # if Resolution == "": Resolution='0'

            if SerialNumber == sensornum:
                inputlist.append((unit,Resolution,Accuracy))

        sensorslist.append([sensorname+'-'+sensornum,sensornum,maker,inputlist])
    return sensorslist

numbers = [2900452, 2901717, 2901702, 2901727, 2900205, 7900239, 2901723, 2901701, 2900451, 2901719, 2901217, 2902585,
           2901707, 2901736, 2901751, 2901749, 2901752, 2901703, 2901753, 2901737, 2901739, 2901708,  2901759,
           2901748, 2901706, 2901744, 2901745, 2901718, 2901721, 2901735,2901725, 2901738, 2900612, 2901734,
           2901724, 2901750, 2901746, 2901757, 2901741, 2901722, 2901720, 2901754, 2901743, 2901732, 2901740, 2901758,
           5904748, 2902054, 2902053, 2901495, 2902451, 2902052, 2902479, 2901572, 2902961, 2902050, 2903183,
           2902980, 2902407, 2902055, 2901570, 2902474, 2902057, 2902051, 2902987, 2902412, 2902491, 2902492,
           2902990, 2903188, 2902480, 2902503, 2903187, 2902502, 2902975, 2902478, 2902518, 2903185, 2901760, 2903186,
           2902958, 5901937, 2902511, 2902692, 2901480, 2902045, 2902693, 2902691, 2901486, 2901482, 2902044, 2902698,
           2902694, 2902695, 2901481, 5904747, 2902697, 2901479, 2902037, 2902696, 2902700, 2902685, 2902962, 2902986,
           2901763, 2901764, 2902555, 5901408, 2902686, 2902549, 2901529, 2902653, 2902656, 2901524, 2902580, 2902683,
           5903429, 2901545, 2902615, 2902562, 2902688, 5901861, 2902655, 5904909, 5901690, 5903749, 2902607, 2902661]
numbers = numbers[0:]
count = 0
for ptfCode in numbers:
    print count, numbers[count-0]
    count += 1
    url = 'http://www.ifremer.fr/co-argoFloats/float?detail=true&ptfCode=' + str(
        ptfCode) + '&sort=PTF_CODE%3AASC&active=true&ocean=P&lang=en'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    # referer='http://www.qiushibaike.com/text/page/'+str(page)
    headers = {'User-Agent': user_agent}
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        text = response.read()

        html = etree.HTML(text)
        stationCode = getStationCode(html)
        stationName = getStationName(html).replace('| ', '')
        description = getDescription(html)
        institution = getInstitution(html)
        project = getProject(html)
        Time = getTime(html)
        loadsensorNamelist = getSensorNamelist(html)
        getSensorNamelist(html)
        processsos.setstation(stationName, stationCode, description, project, institution, Time, loadsensorNamelist)
        sensorslist=getSensors(html)
        for item in sensorslist:
            sensorName=item[0]
            sensornum=item[1]
            maker=item[2]
            uomlist=item[3]
            processsos.setsensor(stationName, stationCode, institution, Time, sensorName, sensornum, maker, uomlist)



    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code, 'page=' + str(ptfCode)
        if hasattr(e, "reason"):
            print e.reason
