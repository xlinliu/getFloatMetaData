# --* coding:utf-8*--
# import numpy as np
#
# A = np.matrix([
#     [1, 1],
#     [2, 0.5],
#     [5, 0.2],
#     [10, 0.1]
# ])
# Y = np.matrix([
#     [8],
#     [7],
#     [10],
#     [21]
# ])
# print (A.T * A).I * (A.T * Y)

#
# class Parent:
#     """
#     parent class
#     """
#
#     def __init__(self):
#         self.attribute1 = 0
#
#     def print_attribute(self):
#         print self.attribute1
#
#
# class Child1(Parent):
#     """
#     Child class 1
#     """
#
#     def __init__(self):
#         Parent.__init__(self)
#         self.attribute1 = 1
#         self.attribute2 = 2
#
#     def print_attribute(self):
#         print self.attribute2
#
#
# parent = Parent()
# child = Child1()
#
# print parent.attribute1
# print child.attribute1
# child.print_attribute()


# class Counter:
#     counter = 0
#
#     def __init__(self):
#         self.counter += 1
#
# print Counter.counter
# c = Counter()
# print c.counter


# class Parent:
#     """
#     parent class
#     """
#
#     def __init__(self):
#         self.attribute1 = 0
#
#     def print_attribute(self):
#         print 'parent'
#
#
# class Child1(Parent):
#     """
#     Child class 1
#     """
#
#     def __init__(self):
#         Parent.__init__(self)
#         self.print_attribute()
#
#     def print_attribute(self):
#         print 'child'
#
# child = Child1()


# f = open('C:\Users\LXL_lib\Desktop\html\DynamicNavigator.html'.decode('utf-8'), 'r')
# for line in f:
#     print line.decode('gbk').encode('utf-8')


# import sys
#
# reload(sys)
# sys.setdefaultencoding('gbk')
#
# str1 = "10°5".decode("utf-8")
# str1 = str1.encode('Latin-1')
# str2 = unicode(str1, 'Latin-1')
# print type(str1)
# print(str1)
# path = r'F:\PythonLearning\resource\workfile'.decode('utf-8')
# f = open(path, 'r+')
# f.write(str1)
# f.flush()
# f.close()


# 测试列表索引返回的内容是一个引用型数据时，返回的是引用还是一份内存拷贝，发现是引用
# l1 = [1, [2, 3]]
# l2 = l1[1]
# l2[0] = 4
# print l1[1]  # [4, 3]

# 测试json模块
# path = r'F:\PythonLearning\resource\workfile'.decode('utf-8')
# f = open(path, 'w')
# x = [1, 'simple', 'list']
#
# import json
#
# json.dump(x, f)
# f.flush()
# f.close()
# f = open(path, 'r')
# y = json.load(f)
# print type(y)

# 在实例变量创建之后，再为实例变量创建函数方法，不需要有self参数，因为此时已经知道了是把函数付给哪一个实例了
# class class1(object):
#     pass
#
#
# c1 = class1()
# c2 = class1()
# class1.__len__ = lambda self: 1
# c2.__len__ = lambda: 2
# print len(c1)
# print len(c2)
#
#
# def func1(x):  # 没有self
#     print 'func1 print:', x
#
#
# c2._attr1 = func1
# class1._attr1 = func1
# print 'c1._attr1:', c1._attr1()
# print 'c2._attr1:', c2._attr1(3)


import re
sourcepath=r"F:\我的下载\THE CEOS DATABASE   INSTRUMENT SUMMARY - MHS.htm".decode('utf-8')
fin=open(sourcepath,'r')
html=fin.read()
outpath=r'F:\我的下载\out.txt'.decode('utf-8')
fout=open(outpath,'w')
pattern = re.compile(r'id="lbl(.*?)">(<a.*?>)?(.*?)<', re.S)
results = re.findall(pattern, html)
for item in results:
    fout.write(item[0] + ':'+item[2])
    fout.write('\n')
fout.write('Instrument Missions:\n')
pattern = re.compile(r'<td><a.*?missionID=\d{3}">(.*?)<sup><img', re.S)
results = re.findall(pattern, html)
for item in results:
    # print item
    fout.write(item)
    fout.write('\n')
fout.close()

