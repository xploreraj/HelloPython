class Node:
    def __init__(self, key):
        self.data = key
        self.rchild = None
        self.lchild = None


def binary_insert(node, key):
    if node is None:
        print('run')
        node = Node(key)
        return node
    else:
        if key < node.data:
            if node.lchild is None:
                node.lchild = Node(key)
            else:
                binary_insert(node.lchild, key)
        else:
            if node.rchild is None:
                node.rchild = Node(key)
            else:
                binary_insert(node.rchild, key)


def in_order_print(root):
    if root is None:
        return
    in_order_print(root.lchild)
    print(root.data)
    in_order_print(root.rchild)


def pre_order_print(root):
    if not root:
        return
    print(root.data)
    in_order_print(root.lchild)
    in_order_print(root.rchild)


if __name__ == '__main__':
    root = Node(3)
    binary_insert(root, 4)
    binary_insert(root, 2)
    binary_insert(root, 7)

    in_order_print(root)