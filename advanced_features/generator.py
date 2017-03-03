#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author = 'shilinlee.com'
g = (x * x for x in range(10))
for n in g:
	print(n)

#斐波拉契数列（Fibonacci）除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
	n, a, b = 0, 0, 1
	while n<max:
		yield b
		a, b = b, a+b
		n = n + 1
	return "done"
#要生成一个generator对象	
f = fib(6)
print(next(f))
print(next(f))
print(next(f))
print(next(f))