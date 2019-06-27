from typing import List
from DataStructure.Node import Node, init_node, print_node

Stack = List


# 利用栈来求解，将链表入栈，出栈时 相加求和，进位，并新建节点
def add_list(head1: Node, head2: Node) -> Node:
    s1: Stack[Node] = list()
    s2: Stack[Node] = list()
    while head1:
        s1.append(head1.value)
        head1 = head1.nexts
    while head2:
        s2.append(head2.value)
        head2 = head2.nexts
    ca: int = 0
    node: Node = None
    while s1 or s2:
        n1 = s1.pop() if s1 else 0
        n2 = s2.pop() if s2 else 0
        n = n1 + n2 + ca
        pre = node
        node = Node(n % 10)
        node.nexts = pre
        ca = n // 10
    if ca == 1:
        pre = node
        node = Node(1)
        node.nexts = pre
    return node


# 第二种方法，先将链表反正，这样就可以从尾部相加求和，进位，并建立链表

if __name__ == '__main__':
    a1 = [1, 2, 3]
    a2 = [2, 7]
    h1 = init_node(a1)
    h2 = init_node(a2)
    h = add_list(h1, h2)
    print_node(h)
