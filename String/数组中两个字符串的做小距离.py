#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 数组中两个字符串的做小距离.py
@Time    : 2019/6/23 17:17
@Author  : hrx
@Email   : hurx1116@gmail.com
"""


def min_distance(strs: list, s1: str, s2: str) -> int:
    if not strs or not s1 or not s2:
        return -1
    if s1 == s2:
        return 0
    last1 = -1
    last2 = -1
    mins = float('inf')
    for idx, s in enumerate(strs):
        if s == s1:
            mins = min(mins, mins if last2 == -1 else idx - last2)
            last1 = idx
        if s == s2:
            mins = min(mins, mins if last1 == -1 else idx - last1)
            last2 = idx
    return -1 if mins == float('inf') else mins


if __name__ == '__main__':
    ss = "1333231"
    s = list(ss)
    m = min_distance(s, '1', '2')
    print(m)
