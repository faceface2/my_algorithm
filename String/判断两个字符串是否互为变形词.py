from typing import Dict, AnyStr

"""
变形词: 如果两个字符串中国出现的字符种类一样且每种字符出现的次数也一样
"""


# 使用map来记录字符出现个数
# 时间复杂度O(N)，空间复杂度O(N)
def is_deformation(str1: str, str2: str) -> bool:
    if not str1 or not str2 or len(str1) != len(str2):
        return False
    mp: Dict[str, int] = dict()
    for i in str1:
        if i not in mp:
            mp[i] = 0
        mp[i] += 1
    for i in str2:
        if mp[i] == 0:
            return False
        mp[i] -= 1
    return True


a = is_deformation('123', '231')

print(a)
