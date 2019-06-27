"""
将字符串中的所有数字相加并求和，如果数字前有减号，奇数个数为负数，偶数个数为正数
s='A1B2C33'             return:36
s2 = 'A-1B--2C--D6E‘    return:7
"""


def main(str1: str) -> int:
    if not str1:
        return 0
    res = 0
    num = 0
    posi = True
    for i in range(len(str1)):
        if not str1[i].isdigit():
            res += num
            num = 0
            if str1[i] == '-':
                if i - 1 > -1 and str1[i - 1] == '-':
                    posi = not posi
                else:
                    posi = False
            else:
                posi = True
        else:
            cur = int(str1[i])
            num = num * 10 + (cur if posi else -cur)
    res += num
    return res



print(main('b1x2c-3d55'))
