# middle of the linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def findMiddle(head):
    slow = head
    fast = head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
    print(findMiddle(head).value)

