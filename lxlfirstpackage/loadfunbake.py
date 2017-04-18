# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time

with open(r'F:\PythonLearning\resource\funbake', 'w') as f:
    for page in range(1, 35):
        url = 'http://www.qiushibaike.com/text/page/' + str(page)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        referer='http://www.qiushibaike.com/text/page/'+str(page)
        headers = {'User-Agent': user_agent,'Referer':referer}
        try:
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            html = response.read()
            pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">'
                                 r'.*?<span>(.*?)</span>', re.S)
            results = re.findall(pattern, html)
            for item in results:
                f.write('作者：'+item[0]+'\n\n')
                f.write(item[1].replace('<br/>', '\n'))
                f.write('\n\n\n++++------------------------------------------------------------------++++\n')
            time.sleep(3)
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code,'page='+str(page)
            if hasattr(e, "reason"):
                print e.reason
f.close()

