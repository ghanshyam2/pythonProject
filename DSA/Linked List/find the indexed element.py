class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        neu_node = Node(new_data)
        neu_node.next = self.head
        self.head = neu_node

    def printList(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next

    def indexed_element(self, index):

        count = 0
        curr = self.head
        while curr is not None:

            if count == index:
                return curr.data
            count += 1
            curr = curr.next
        return 0


llist = LinkedList()
llist.push(1)
llist.push(4)
llist.push(1)
llist.push(12)
llist.push(1)
llist.push(5)
print(llist.indexed_element(6))


