from typing import List
from DataStructure.Node import Node, init_node, print_node


def main(head: Node) -> bool:
    """
    使用栈，将链表二分，右半边部分放进栈，然后出栈与左边部分比较
    """
    if not head or not head.nexts:
        return False

    cur: Node = head
    right: Node = head.nexts
    while cur.nexts and cur.nexts.nexts:
        right = right.nexts
        cur = cur.nexts.nexts
    stack: List = list()
    while right:
        stack.append(right)
        right = right.nexts
    while stack:
        if head.value != stack.pop().value:
            return False
        head = head.nexts
    return True


def is_palindrome3(head: Node) -> bool:
    """
    将链表二分，调整右半边的指向，然后左右两边依次比较
    1->2->3<-1<-2
    :param head:
    :return:
    """
    if not head or not head.nexts:
        return False

    n1: Node = head
    n2: Node = head
    while n2.nexts and n2.nexts.nexts:
        n1 = n1.nexts
        n2 = n2.nexts.nexts
    n2 = n1.nexts
    n1.nexts = None
    while n2:
        n3 = n2.nexts
        n2.nexts = n1
        n1 = n2
        n2 = n3
    n3 = n1
    n2 = head
    res: bool = True
    while n1 and n2:
        if n1.value != n2.value:
            res = False
        n1 = n1.nexts
        n2 = n2.nexts
    n1 = n3.nexts
    n3.nexts = None
    while n1:
        n2 = n1.nexts
        n1.nexts = n3
        n3 = n1
        n1 = n2
    return res


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 2, 1]
    head = init_node(arr)
    # print_node(head)
    # s = remove_middle_node(head)
    # print_node(s)
    s = is_palindrome3(head)
    print(s)
