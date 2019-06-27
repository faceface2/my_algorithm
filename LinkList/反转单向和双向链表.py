from DataStructure import Node, DoubleNode, init_node, print_node, init_double_node, print_double_node


# 1 2 3 4
def reverse_list(head: Node):
    pre: Node = None
    while head:
        nexts = head.nexts
        head.nexts = pre
        pre = head
        head = nexts
    return pre


# 1 2 3 4
def reverse_double_list(head: DoubleNode) -> DoubleNode:
    pre: DoubleNode = None
    while head:
        nexts = head.nexts
        head.nexts = pre
        head.last = nexts
        pre = head
        head = nexts
    return pre


def main():
    a = [1, 2, 3, 4, 5]
    # h = init_node(a)
    # h = reverse_list(h)
    # print_node(h)
    h = init_double_node(a)
    print_double_node(h)
    h = reverse_double_list(h)
    print_double_node(h)


if __name__ == '__main__':
    main()
