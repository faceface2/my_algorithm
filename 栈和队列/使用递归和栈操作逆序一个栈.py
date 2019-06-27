def getAndreoveLastElement(stack: list):
    result = stack.pop()
    if not stack:
        return result
    else:
        last = getAndreoveLastElement(stack)
        stack.append(result)
        return last


def reverse(stack: list):
    if not stack:
        return
    t = getAndreoveLastElement(stack)
    reverse(stack)
    stack.append(t)


s = [1, 2, 3, 4, 5]
reverse(s)
print(s)


class AAAA:
    def __init__(self):
        pass

    @staticmethod
    def add():
        ...
