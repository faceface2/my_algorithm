from Node import Node


def relocate(head: Node) -> None:
    if not head or not head.next:
        return
    mid = head
    right = head.next
    while right.next and right.next.next:
        mid = head.next
        right = right.next.next
    right = mid.next
    mid.next = None
    merge(head, right)


def merge(left: Node, right: Node) -> None:
    while left.next:
        nexts = right.next
        right.next = left.next
        left.next = right
        left = right.next
        right = nexts
    left.next = right


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.next = c
    c.next = d
    relocate(a)
    while a:
        print(a.value)
        a = a.next