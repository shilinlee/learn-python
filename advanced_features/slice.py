#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author = 'shilinlee.com'

#切片（Slice）操作符
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#从索引0开始，到3结束，但不包括3
print("前3个数据：",L[0:3])

# 0可以省略
print("最后2个数据：",L[-2:])

L = list(range(100))
print("前11-20个数：",L[10:20])
print("所有数，每5个取一个：",L[::5])

#对字符串切片
print('ABCDEFG'[:3])