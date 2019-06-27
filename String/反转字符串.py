#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 反转字符串.py
@Time    : 2019/6/23 16:55
@Author  : hrx
@Email   : hurx1116@gmail.com
"""
"""
1
    s = "hello world" 
    :return "world hello"
2
    s = "ABCDE" size = 3
    :return "DEABC"
"""


def reverse(chas, s, e):
    while s < e:
        chas[s], chas[e] = chas[e], chas[s]
        s += 1
        e -= 1


def rotate_word(chas: list):
    if not chas:
        return
    reverse(chas, 0, len(chas) - 1)
    l = -1
    r = -1
    for i in range(len(chas)):
        if chas[i] != ' ':
            l = i if i == 0 or chas[i - 1] == ' ' else l
            r = i if i == (len(chas) - 1) or chas[i + 1] == ' ' else r
        if l != -1 and r != -1:
            reverse(chas, l, r)
            l = -1
            r = -1


def rotate_word2(chas: list, size: int):
    if not chas or size < 0 or size > len(chas):
        return
    reverse(chas, 0, size - 1)
    reverse(chas, size, len(chas) - 1)
    reverse(chas, 0, len(chas) - 1)


if __name__ == '__main__':
    a = 'hello world hu!'
    s = list(a)
    rotate_word(s)
    print(str(s))
    b = ['A','B','C','D','E']
    rotate_word2(b, 3)
    print(b)
