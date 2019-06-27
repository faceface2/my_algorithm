from BST import BST
from queue import Queue
from typing import List

def convert(head: BST)->BST:
    mq = Queue()
    in_order_to_queue(head, mq)
    if mq.empty():
        return head
    head = mq.get()
    pre = head
    pre.left = None
    while not mq.empty():
        curr = mq.get()
        pre.right = curr
        curr.left = pre
        pre = curr
    pre.right = None
    return head


def in_order_to_queue(head: BST, que: Queue):
    if not head:
        return
    in_order_to_queue(head.left, que)
    que.put(head)
    in_order_to_queue(head.right, que)


if __name__ == '__main__':
    a = BST(1)
    b = BST(2)
    c = BST(3)
    b.left = a
    b.right = c
    d = convert(b)
    while d:
        print(d.value)
        d = d.right