from String.KMP import KMP


def is_rotation(a: str, b: str) -> bool:
    if not a or not b or len(a) != len(b):
        return False
    c = b + b
    return KMP(c, a)


if __name__ == '__main__':
    print(is_rotation('abcd', 'cdab'))
    float()
