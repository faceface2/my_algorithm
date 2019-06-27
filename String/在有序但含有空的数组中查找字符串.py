"""
strs中的字符串是按照字典顺序有小到大依次出现
返回str在strs中出现的最左的位置
strs = ['s',None,'r',None,'c'] str='s', return:0
"""


def getIndex(strs: list, s: str) -> int:
    if not strs or not s:
        return -1
    res: int = -1
    left: int = 0
    right: int = len(strs) - 1
    while left <= right:
        mid = (left + right) // 2
        if strs[mid] == s:      # 如果strs[mid]==s,说明找到s，令res=mid，但需要找最左位置，所以需要令right=mid-1，看有没有更左的s
            res = mid
            right = mid - 1
        elif strs[mid]:         # 如果strs[mid]与s不同，比较strs[mid]与s，如果mid小于s，说明左边不会出现str，需要在右边查找，大于亦然
            if strs[mid] < s:
                left = mid + 1
            else:
                right = mid - 1
        else:                   # 如果strs[mid]为None，
            i = mid
            while not strs[i]:  # 从mid开始，从右到左遍历左半区
                i -= 1
                if not (i >= left):
                    break
            if i < left or strs[i] < s:     # 如果左半区为空，则遍历右半区或者strs[i]小于s，
                left = mid + 1
            else:
                res = i if strs[i] == s else res    # 若strs[i]== s，更新res
                right = i - 1                       # 若strs[i] > s,调整指针
    return res


if __name__ == '__main__':
    s = ['a', None, 'c', 'f', None, 'h', None, None, 'k', 'z']
    print(getIndex(s, 'c'))
