#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#author "shilinlee"
import urllib.request
from city import city
import json

cityname = input('你想查哪个城市的天气？\n')
citycode = city.get(cityname)
if citycode:
	try:
		url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
		content = urllib.request.urlopen(url).read()
		weather = bytes.decode(content)
		print(weather)
		data = json.loads(weather)
		print(data)
		result = data['weatherinfo']
		str_temp = ('%s\n%s ~ %s') % (result['weather'],result['temp1'],result['temp2'])
		print(str_temp)
	except:
		print("查询失败")
else:
	print("没有找到该城市")