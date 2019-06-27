from typing import List


def maxRecSize2(maps: List[List]):
    if not maps or not maps[0]:
        return
    max_area: int = 0
    height: List[int] = [0] * len(maps[0])
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            height[j] = 0 if maps[i][j] == 0 else height[j] + 1
            max_area = max(max_area, maxRecFromBottom2(height))
    return max_area


def maxRecFromBottom2(height: List) -> int:
    if not height:
        return 0
    max_area = 0
    stack: List[int] = []
    for i in range(len(height)):
        while stack and height[i] <= height[stack[-1]]:
            j = stack.pop()
            k = stack[-1] if stack else -1
            cur_area = (i - k - 1) * height[j]
            max_area = max(max_area, cur_area)
        stack.append(i)
    while stack:
        j = stack.pop()
        k = stack[-1] if stack else -1
        cur_area = (len(height) - k - 1) * height[j]
        max_area = max(max_area, cur_area)
    return max_area


a = [
    [1, 0, 1, 1],
    [1, 1, 1, 1],
]

s = maxRecSize2(a)
print(s)
