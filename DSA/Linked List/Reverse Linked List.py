class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def reverseList(self):
        curr = self.head
        prev = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def push(self, newNode):
        new_node = Node(newNode)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        node = self.head

        while node:
            print(node.data, end=' ')
            node = node.next


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given linked list")
llist.printList()
llist.reverseList()
print("\nReversed linked list")
llist.printList()