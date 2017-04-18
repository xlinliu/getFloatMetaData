# coding:utf-8
import mysql.connector
import datetime
import random
from mysql.connector import errorcode

province = ['hunan', 'hubei', 'guangdong', 'fujian', 'shandong', 'yunnan', 'shanxi', 'chongqing', 'henna', 'hebei',
            'shanghai'
    , 'beijing', 'jiangxi', 'guizhou', 'jiangsu', 'sichuan', 'tianjing', 'ningxia', 'xinjiang', 'neimeng']
city = ['wuhan', 'huangshi', 'shiyan', 'ganzhou', 'yintang', 'fuzhou', 'changsha', 'xinyu', 'shangrao', 'huanggang',
        'xianning'
    , 'zhuzhou', 'taizhou', 'nanjing', 'hangzhou', 'xiangtang', 'xiangfang', 'taiyuan', 'quanzhou', 'fuzhou']
pnum = len(province)
cnum = len(city)


def select(cur):
    print '查询前时间：', datetime.datetime.now()
    sql = 'SELECT count(*) FROM testtable WHERE province="hunan" AND city="changsha"'
    cur.execute(sql)
    values = cur.fetchall()
    print '查询后时间：', datetime.datetime.now()
    return values


def insertdata(cut):
    print '插入第二个一千万条数据之前的时间：', datetime.datetime.now()
    try:
        for i in xrange(10000000):
            value1 = province[random.randint(0, pnum - 1)]
            value2 = city[random.randint(0, cnum - 1)]
            sql = 'INSERT INTO testtable ( province, city ) VALUES ( "' + value1 + '","' + value2 + '")'
            cur.execute(sql)
    except mysql.connector.Error as e:
        print('create table orange fails!{}'.format(e))
    print '插入第二个一千万条数据之后的时间：', datetime.datetime.now()
    conn.commit()


conn = mysql.connector.connect(user='root', password='kexue666821', host='127.0.0.1', database='TESTINDEX')
cur = conn.cursor()
result = select(cur)
print '查询结果是：',result
# insertdata(cur)
cur.close()
conn.close()
