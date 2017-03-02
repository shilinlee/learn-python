#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author = 'shilinlee.com'
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
#默认dict 迭代的是key
for key in d:
	print(key)

#迭代dict 的 value
for value in d.values():
	print(value)

#同时迭代key和value
for k,v in d.items():
	print(k,"=>",v)

#判断对象是否是可迭代的数据类型
print(isinstance('abc', Iterable))  #True

#把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
	print(i, "=>",value)
