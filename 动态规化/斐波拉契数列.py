#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 斐波拉契数列.py
@Time    : 2019/6/26 20:04
@Author  : hrx
@Email   : hurx1116@gmail.com
"""


# 斐波拉契数列
def fib(n: int) -> int:
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    res = 1
    pre = 1
    for i in range(3, n + 1):
        res, pre = res + pre, res
    return res


# 跳台阶问题
def s1(n: int) -> int:
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return s1(n - 1) + s1(n - 2)


def s2(n: int) -> int:
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return n
    res = 2
    pre = 1
    for i in range(3, n + 1):
        res, pre = res + pre, res
    return res


# 农场中的牛问题
def c1(n: int) -> int:
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    return c1(n - 1) + c1(n - 3)


def c2(n: int) -> int:
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    res = 3
    pre = 2
    ppre = 1
    for i in range(4, n + 1):
        res, pre, ppre = res + ppre, res, pre
    return res


if __name__ == '__main__':
    print(fib(6))
    print(c2(6))
