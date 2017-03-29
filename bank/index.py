#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#author "shilinlee.com"
#1.爬虫
#2.写入Excel
import urllib,re  # requests 
import xlwt #学如excel

def getData():
	url_list = []
	for i in range(1,10):
		url = "http://furhr.com/?page={}".format(i)
		try:
			html = urllib.urlopen(url).read()
		except Exception as e:
			print e
			continue
		#w = re.compile() #编译 提高效率
		page_list = re.findall(r'<tr><td>\d+</td><td>\d+</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',html)
		#print page_list[0][0].decode("utf-8")
		url_list.append(page_list)
		#print page_list
	return url_list
def excel_write(items):
	newTable = "test123.xls"
	wb = xlwt.Workbook(encoding="utf-8") #创建文件 设置编码
	ws = wb.add_sheet("test1") #创建表
	headData = ['公司名称','电话','地址']
	for colnum in range(0,3):
		ws.write(0,colnum,headData[colnum],xlwt.easyxf("font: bold on")) # 0行，列，内容
	wb.save(newTable) #保存
	print "创建成功".decode("utf-8")

	#写入数据
	index = 1
	for item in items:
		for j in range(0,len(item)):
			for i in range(0,3):
				ws.write(index,i,item[j][i])
			index += 1
		wb.save(newTable) #保存

if __name__ == '__main__': #判断文件入口
	items = getData()
	excel_write(items)