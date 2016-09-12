'''
You’re given a binary tree. Let’s print this tree in inward spiral order, i.e.
First you print all nodes at level 1,
then all nodes in level n (lowest node),
then all nodes in level 2, …
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def print_inward_spiral(node):
    top = 1
    bottom = height(node)
    # ltr = True
    while top <= bottom:
        print_level(node, top, False)
        if top != bottom:
            print_level(node, bottom, True)
        top += 1
        bottom -= 1


def print_level(node, level, ltr):
    if node is None:
        return
    if level is 1:
        print(node.data)
    elif level > 1:
        if ltr:
            print_level(node.left, level - 1, ltr)
            print_level(node.right, level - 1, ltr)
        else:
            print_level(node.right, level - 1, ltr)
            print_level(node.left, level - 1, ltr)


# driver
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
# root.right.right.left = Node(8)

print_inward_spiral(root)
