import math
from DataStructure import Node, init_node, print_node


def remove_middle_node(head: Node):
    if not head or not head.nexts:
        return head
    if not head.nexts.nexts:
        return head.nexts
    pre: Node = head
    cur: Node = head.nexts.nexts
    while cur.nexts and cur.nexts.nexts:
        pre = pre.nexts
        cur = cur.nexts.nexts
    pre.nexts = pre.nexts.nexts
    return head


def remove_by_ratio(head: Node, a: int, b: int) -> Node:
    """
    计算链表长度，删除节点的公式为 (a*n)/b
    :param head:
    :param a:
    :param b:
    :return:
    """
    if a < 1 or a > b:
        return head
    n: int = 0
    curr: Node = head
    while curr:
        n += 1
        curr = curr.nexts  # 链表长度
    n = math.ceil((a * n) / b)
    if n == 1:
        head = head.nexts
    if n > 1:
        curr = head
        n -= 1
        while n != 1:
            curr = curr.nexts
            n -= 1
        curr.nexts = curr.nexts.nexts
    return head


if __name__ == "__main__":
    arr = [3, 5, 1, 6, 9, 4, 8]
    head = init_node(arr)
    # print_node(head)
    # s = remove_middle_node(head)
    # print_node(s)
    s = remove_by_ratio(head, 5, 6)
    print_node(s)
