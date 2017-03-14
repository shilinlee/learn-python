#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author = 'shilinlee.com'
#返回奇数
def is_odd(n):
	return n%2==1

L = list(filter(is_odd,[1,2,3,4,5,7,8,12,15]))
print(L)

#去掉空字符串
def not_empty(s):
	return s and s.strip()
L = list(filter(not_empty,['A','','B',None,'C',' ']))
print(L)