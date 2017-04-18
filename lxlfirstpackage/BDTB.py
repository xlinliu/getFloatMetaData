import mysql.connector
import urllib
import re
import urllib2


class QuestionList(object):
    def __init__(self, indexurl):
        self.__indexurl = indexurl
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        request = urllib2.Request(self.__indexurl, headers=headers)
        self.response = urllib2.urlopen(request)
        self.indexpage = self.response.read()
        self.question_list = self.__find_question_list(self.indexpage)
        self.host = request.get_host()

    def write_indexpage2file(self, path):
        file = open(path, 'w')
        file.write(self.indexpage)

    @staticmethod
    def __find_question_list(indexpage):
        pattern = re.compile(r'question-title(.*?)href="(.*?)"(.*?)>(.*?)</a>', re.S)
        results = re.findall(pattern, indexpage)
        question_list = []
        for item in results:
            question_list.append((item[1], item[3]))
        return question_list


def get_anser(referer, url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent, 'Referer': referer}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    anser_page = response.read()


if __name__ == "__main__":
    pagetest = QuestionList('http://iask.sina.com.cn/c/187.html')
    # pagetest.write_indexpage2file(r'F:\PythonLearning\resource\csdn')
    for item in pagetest.question_list:
        print item[0], item[1]

# cnx = mysql.connector.connect(user='root', password='kexue666821',host='127.0.0.1',database='geosmarter')
# cnx.close()
