"""
给定字符串str和整数k，如果str中正好有连续的k个0出现，把k个0字符去掉，返回处理后的字符串
s='a00b' k=2  return: ab
时间复杂度：O(N)
空间复杂度：O(1)
"""


def main(str1: str, k: int) -> str:
    if not str1 or k < 1:
        return str1
    count = 0
    start = -1
    str2 = list(str1)
    for idx, i in enumerate(str2):
        if i == '0':
            count += 1
            start = idx if start == -1 else start
        else:
            if count == k:
                while count != 0:
                    str2[start] = ''
                    start += 1
                    count -= 1
            count = 0
            start = -1
    if count == k:
        while count != 0:
            str2[start] = ''
            count -= 1
            start += 1

    return ''.join(str2)


print(main('a000b00', 2))
