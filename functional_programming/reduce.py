#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author = 'shilinlee.com'
from functools import reduce
#reduce函数必须接收两个参数，结果继续和序列的下一个元素做累积计算
def add(x,y):
	return x + y
print(reduce(add,[1,3,5,9,11,13,15]))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('124235'))
