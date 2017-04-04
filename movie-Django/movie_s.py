#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import urllib,re
from dy.models import DyModels
# import MySQLdb
#
# conn = MySQLdb.connect(
#     host = '127.0.0.1',
#     port = 3306,
#     user='django',
#     password='django',
#     db='dy_dymodels',
#     charset = 'utf8',
# )
# cur = conn.cursor()

def getList(pn):
    html = urllib.urlopen('http://www.piaohua.com/html/dianying.html').read()
    reg = r'<li><a href="(.*?)"class="img"'
    return re.findall(reg,html)[1:]
def getContent(url):
    html = urllib.urlopen('http://www.piaohua.com%s' % url).read()
    reg = r'<h3>(.*?)</h3>'
    title = re.findall(reg,html)[0]
    reg = r'下载页面</div>(.*?)<strong><span style="color: #ff0000">'
    reg = re.compile(reg,re.S) #编译正则表达式
    content = re.findall(reg,html)[0]
    reg = r'line-height: 18px" width="100%"><a href="(.*?)"'
    link = re.findall(reg,html)[0]
    return title,content,link


def saveMovies():
    for i in getList(1):
        title,content,link = getContent(i)
        print '正在保存第%d页的%s' % (1,title)
        dymodel = DyModels(title=title,content=content,link=link)
        dymodel.save()
        # cur.execute("insert into movie(id,title,content,link)")
        # conn.commmit()