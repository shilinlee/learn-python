#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author = 'shilinlee.com'
from operator import itemgetter

print(sorted([36, 5, -12, 9, -21])) #默认从小到大
print(sorted([36, 5, -12, 9, -21], key=abs)) #按照绝对值 从小到大

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)) #忽略首字母大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)) #忽略首字母大小写, 反向排序

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students,key=itemgetter(0)))