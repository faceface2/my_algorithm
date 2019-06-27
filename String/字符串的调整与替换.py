#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 字符串的调整与替换.py
@Time    : 2019/6/23 16:12
@Author  : hrx
@Email   : hurx1116@gmail.com
"""


def modify(chas: list):
    if not chas:
        return
    j = len(chas) - 1
    for i in range(len(chas) - 1, 0, -1):
        if chas[i] != '*':
            chas[j] = chas[i]
            j -= 1
    while j > -1:
        chas[j] = '*'
        j -= 1


if __name__ == '__main__':
    a = ['1', '2', '*', '*', '3', '4', '5']
    modify(a)
    print(a)
