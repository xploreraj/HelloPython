class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def height_of_tree(node):
    if node is None:
        return 0
    return 1 + max(height_of_tree(node.left), height_of_tree(node.right))


def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.data)
    print_inorder(node.right)


def print_spiral(node):
    h = height_of_tree(node)
    dir_ltr = False
    for i in range(1, h+1):
        print_level(node, i, dir_ltr)
        dir_ltr = not dir_ltr


def print_level(node, level, dir_ltr):
    if node is None:
        return
    if level is 1:
        # This means that we have reached the given level from root. Now print this node/leaf data.
        print(node.data)
    elif level > 1:
        if dir_ltr:
            # for same level, call recursively
            print_level(node.left, level-1, dir_ltr)
            print_level(node.right, level-1, dir_ltr)
        else:
            print_level(node.right, level-1, dir_ltr)
            print_level(node.left, level-1, dir_ltr)

# driver
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)

# print_inorder(root)
print_spiral(root)
