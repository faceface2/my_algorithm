from Tree import Tree

def morrisIn(head: Tree):
    # 中序遍历
    if not head:
        return
    cur1 = head
    while cur1:
        cur2 = cur1.left
        if cur2:
            while cur2.right and cur2.right != cur1:
                cur2 = cur2.right
            if not cur2.right:
                cur2.right = cur1
                cur1 = cur1.left
                continue
            else:
                cur2.right = None
        print(cur1.value, end=' ')
        cur1 = cur1.right

def morrisIn2(head: Tree):
    # 先序遍历
    if not head:
        return
    cur1 = head
    while cur1:
        cur2 = cur1.left
        if cur2:
            while cur2.right and cur2.right != cur1:
                cur2 = cur2.right
            if not cur2.right:
                cur2.right = cur1
                print(cur1.value, end=' ')
                cur1 = cur1.left
                continue
            else:
                cur2.right = None
        else:
            print(cur1.value, end=' ')
        cur1 = cur1.right

if __name__ == '__main__':
    a = Tree(1)
    b = Tree(2)
    c = Tree(3)
    d = Tree(4)
    e = Tree(5)
    f = Tree(6)
    g = Tree(7)
    a.left = b
    a.right = c
    b.left= d
    b.right = e
    c.left = f
    c.right = g
    morrisIn(a)
    print('')
    morrisIn2(a)