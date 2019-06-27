# def main():
# #     n = input()
# #     a = [int(i) for i in input().split()]
# #     b = [int(i) for i in input().split()]
# #     a = sorted(a)
# #     b = list(reversed(sorted(b)))
# #     print(sum(i * j for i, j in zip(a, b)))
# # main()

# def main():
#     n, d = [int(i) for i in input().split()]
#     if n > 1 or n > 200000 or d < 1 or d > 100000000:
#         return
#     arr = dict()
#     for i in range(n):
#         a, b = [int(i) for i in input().split()]
#         arr[a] = b
#     n, d = 6, 3
#
#     max_value = 0
#     for item in arr:

# def cmp(a, b):
#     return a[0] - b[0]
# arr = [ [3, 5],[1, 1], [4, 8], [6, 4], [10, 3], [11, 2]]
#
# import functools
# arr = sorted(arr, key=functools.cmp_to_key(cmp))
# print(arr)

# def main():
#     vec = [0]*256
#     visited = [False] * 256
#     s = 'xaBXY'
#     s = s.lower()
#     for c in s:
#         vec[ord(c)] += 1
#     res = []
#     for c in s:
#         vec[ord(c)] -= 1
#         if visited[ord(c)]:
#             continue
#         else:
#             while res and vec[ord(res[0])] > 0 and c < res[0]:
#                 visited[ord(res[0])] = False
#                 res.pop()
#             res.append(c)
#             visited[ord(c)] = True
#     print(''.join(res))
#
# main()

# class GreateMe:
#     def __init__(self, name):
#         self.name = name
#
#     def __getattr__(self, item):
#         allowed = ['hello', 'bye']
#
#         def call_(name=None):
#             if item in allowed:
#                 greeting = item.replace('_', ' ')
#                 target = name if name else self.name
#                 return f'{target},{greeting.capitalize()}'
#             else:
#                 raise ValueError(f'Invalid name or greeting.')
#         return call_
#
# greet = GreateMe('Lina')
# print(greet.hello())
