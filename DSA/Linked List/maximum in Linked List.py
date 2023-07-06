class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newNode):
        new_node = Node(newNode)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        node = self.head

        while node:
            print(node.data, end=' ')
            node = node.next

    def maxLinkedList(self):
        curr = self.head
        maxNum = 0

        while curr:
            if curr.data > maxNum:
                maxNum = curr.data
            curr = curr.next
        return maxNum


llist = LinkedList()
llist.push(1)
llist.push(4)
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(5)
print(llist.maxLinkedList())
