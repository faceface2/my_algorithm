#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 添加最少字符使字符串整体都是回文字符串.py
@Time    : 2019/6/24 13:09
@Author  : hrx
@Email   : hurx1116@gmail.com
"""
from typing import List


def get_dp(string: str):
    dp: List[List[int]] = [[0] * len(string) for _ in range(len(string))]
    for j in range(1, len(string)):
        dp[j - 1][j] = 0 if string[j - 1] == string[j] else 1
        for i in range(j - 2, -1, -1):
            if string[i] == string[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
    return dp


def get_palindrome1(string: str):
    if not string or len(string) < 2:
        return string
    dp = get_dp(string)
    res: List = [None] * (len(string) + dp[0][len(string) - 1])
    i = 0
    j = len(string) - 1
    resl = 0
    resr = len(res) - 1
    while i <= j:
        if string[i] == string[j]:
            res[resl] = string[i]
            res[resr] = string[j]
            i += 1
            j -= 1
        elif dp[i][j - 1] < dp[i + 1][j]:
            res[resl] = string[j]
            res[resr] = string[j]
            j -= 1
        else:
            res[resl] = string[i]
            res[resr] = string[i]
            i += 1
        resl += 1
        resr -= 1
    return ''.join(res)


if __name__ == '__main__':
    print(get_palindrome1('b121c'))
