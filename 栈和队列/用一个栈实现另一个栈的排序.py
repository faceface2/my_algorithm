from typing import List

Stack = List[int]


def sort_stack_by_stack(stack: Stack) -> None:
    help_stack: Stack = []
    while stack:
        cur: int = stack.pop()
        while help_stack and help_stack[-1] < cur:
            stack.append(help_stack.pop())
        help_stack.append(cur)
    while help_stack:
        stack.append(help_stack.pop())


if __name__ == '__main__':
    test = [3, 2, 5, 1, 7]
    sort_stack_by_stack(test)
    print(test)
