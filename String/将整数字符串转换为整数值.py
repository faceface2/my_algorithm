from typing import *


def isvalid(chas: str) -> bool:
    if chas[0] != '-' and (chas[0] < '0' or chas[0] > '9'):
        return False
    if chas[0] == '-' and (len(chas) == 1 or chas[0] == '0'):
        return False
    if chas[0] == '0' and len(chas) > 1:
        return False
    return chas[1:].isdigit() if chas[0] == '-' else chas.isdigit()


def convert(string: str) -> int:
    if not str:
        return 0
    if not isvalid(string):
        return 0
    posi: bool = False if string[0] == '-' else True  # 判断是否有符号位
    minq: int = pow(-2, 31) // 10  # 最小值除以10，防止res乘以10超出大小，
    minr: int = pow(-2, 31) % -10  # 最小值对10取余的余数，防止加上某个数超出大小，
    min_int32 = pow(-2, 31)
    res: int = 0
    for i in string[0 if posi else 1:]:
        curr = -int(i)
        if (res < minq) or (res == minq and curr < minr):
            return 0
        res = res * 10 + curr
    if posi and res == min_int32:
        return 0
    return -res if posi else res


if __name__ == '__main__':
    print(convert('-2147483648'))
