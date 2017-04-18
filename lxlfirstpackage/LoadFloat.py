# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from lxml import etree

f = open(r'F:\PythonLearning\resource\float' + '.html', 'w')
f.write("<data>")
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
for ptfCode in numbers:
    f.write("<sensor>")
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
        # result = etree.tostring(html)
        # print type(html)
        div = html.xpath("//div[@class='floatInfo']")[0]
        dataTable = div.xpath("child::table[@class='data']")[0]
        datas = dataTable.xpath("descendant::tr[@class='code' or @class='name' or @class='description'"
                                "or @class='project' or @class='institution' or @class='dac' "
                                "or @class='first-cycle-date']")
        realData = datas[0:len(datas) - 1]
        print len(datas)

        for data in realData:
            result = etree.tostring(data)
            f.write(result)


        f.write("</sensor>")
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code, 'page=' + str(ptfCode)
        if hasattr(e, "reason"):
            print e.reason
f.write("</data>")
f.close()
