#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author = 'shilinlee.com'
def f(x):
	return x * x
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

print(list(map(str,[1,2,3,4,5,6])))
