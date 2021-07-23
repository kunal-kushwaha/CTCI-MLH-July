from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    ans = []

    if root is None:
        return ans

    q = deque()
    q.append(root)

    while q:
        level = len(q)
        current = []
        for l in range(level):
            removed = q.popleft()
            current.append(removed.value)
            if removed.left:
                q.append(removed.left)
            if removed.right:
                q.append(removed.right)
        
        # here the level is finished
        # append in original ans
        ans.append(current)

    return ans

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(bfs(root))