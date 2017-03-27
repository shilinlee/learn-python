#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#author "shilinlee"
data  = "write some thing new!"
f1 = open("data.txt")
data1 = f1.read()
f1.close()

f2 = open("data2.txt","w") # w 可以换成 a (追加内容)
f2.write(data1)
f2.close()