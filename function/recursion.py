#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 利用递归函数计算阶乘
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

print('fact(1) = ',fact(1))
print('fact(5) = ',fact(5))
