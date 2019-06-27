import sys


def main(str1: str, str2: str) -> int:
    if not str1 or not str2 or len(str1) < len(str2):
        return 0
    maps = [0] * 256
    left, right = 0, 0
    match = len(str2)
    minLen = float('inf')
    for i in str2:
        maps[ord(i)] += 1
    while right < len(str1):
        maps[ord(str1[right])] -= 1
        if maps[ord(str1[right])] >= 0:
            match -= 1
        if match == 0:
            while maps[ord(str1[left])] < 0:
                maps[ord(str1[left])] += 1
                left += 1
            minLen = min(minLen, right - left + 1)
            match += 1
            maps[ord(str1[left])] += 1
            left += 1
        right += 1
    return 0 if minLen == float('-inf') else minLen

print(main('abcde', 'ac'))
# abacdedc