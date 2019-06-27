"""
aaabbaddd
return: a_3_b_2_a_1_d_3
"""


def get_count_string(string: str) -> str:
    if not string:
        return ""
    res = string[0]
    num: int = 0
    for idx, s in enumerate(string):
        if idx == 0 or s == string[idx - 1]:
            num += 1
        else:
            res = res + '_' + f'{num}' + '_' + s
            num = 1
    return res + '_' + f'{num}'


print(get_count_string("aaabbaddd"))
