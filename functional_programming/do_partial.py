#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author = 'shilinlee.com'
import functools

# functools.partial：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
int2 = functools.partial(int,base=2)
print(int2("10000"))