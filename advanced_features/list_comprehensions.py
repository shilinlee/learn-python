#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author = 'shilinlee.com'
import os # 导入os模块

#快速生成列表
L = [x * x for x in range(1, 11)]
print("列表：",L)

#加上条件判断
L = [x * x for x in range(1,11) if x%2 == 0]
print("条件列表：",L)

#两层循环
L = [m+n for m in 'ABC' for n in '123']
print("两层循环列表",L)

L = [d for d in os.listdir('.')]
print("所有文件和目录名",L)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str) == True]
print("将字母变小写",L2)