#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#author "shilinlee"

f = open("data.txt")
data = f.read()
print(data)
lines = f.readlines()
print(lines)
f.close()