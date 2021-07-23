class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def hasPath(root, sum):
    if root is None:
        return False
    
    # if it is a leaf node with req sum = value of the node itself
    if root.value == sum and root.left is None and root.right is None:
        return True

    return hasPath(root.left, sum - root.value) or hasPath(root.right, sum - root.value)



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(hasPath(root, 19))