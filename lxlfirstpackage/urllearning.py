# --* encoding:utf-8 *--
import urllib
import urllib2
import cookielib

# values = {"username": "1016903103@qq.com", "password": "XXXX"}
# data = urllib.urlencode(values)
# url = "http://127.0.0.1:8080/cba/"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
#
# f = open(r'F:\PythonLearning\resource\就分.html'.decode('utf-8'), 'w')
# f.write(response.read())
cookie = cookielib.MozillaCookieJar(r'F:\PythonLearning\resource\workfile')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'stuid': '201200131012',
    'pwd': '23342321'
})
# 登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# 模拟登录，并把cookie保存到变量
result = opener.open(loginUrl, postdata)
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
f = open(r'F:\PythonLearning\resource\就分.html'.decode('utf-8'), 'w')
f.write(result.read())
# 利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# 请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()
