from typing import Any, List

Stack = List


def get_and_remove_element(stack: Stack) -> Any:
    """
    递归查找栈底元素并返回
    :param stack:
    :return:
    """
    result = stack.pop()
    if not stack:
        return result
    else:
        last = get_and_remove_element(stack)
        stack.append(result)
        return last


def reverse_stack(stack: Stack) -> None:
    if not stack:
        return
    last = get_and_remove_element(stack)  # 获取栈底元素保存在递归变量里，最后从栈顶元素开始插入并结束递归
    reverse_stack(stack)
    stack.append(last)


def main():
    s: List[str] = [1, 2, 3]
    s.append(5)
    reverse_stack(s)
    s1 = [1, 2]
    reverse_stack(s1)
    s2 = [1]
    reverse_stack(s2)
    s3 = []
    reverse_stack(s3)
    print(s)
    print(s1)
    print(s2)
    print(s3)


main()
