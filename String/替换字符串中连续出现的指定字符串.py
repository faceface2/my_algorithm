"""
给定三个字符串str、from、to，把str中所以from子串全部替换成to字符串，连续出现的from只替换成一个to字符串
"""

from typing import *


def clear(chas, i, length):
    while length != 0:
        chas[i] = ''
        i -= 1
        length -= 1


def repleac(string: str, frm: str, to: str) -> str:
    if not string or not frm:
        return string
    chas: List[str] = list(string)
    chaf: List[str] = list(frm)
    match: int = 0
    for idx, s in enumerate(chas):
        if chas[idx] == chaf[match]:
            match += 1
            if match == len(chaf):
                clear(chas, idx, len(chaf))
                match = 0
        else:
            match = 0
    res: str = ''
    for idx, cha in enumerate(chas):
        if cha:
            res += cha
        if not cha and (idx == 0 or chas[idx - 1]):
            res += to
    print(res)
    return res


print(repleac('ab123123cdab', 'ab', '45'))
