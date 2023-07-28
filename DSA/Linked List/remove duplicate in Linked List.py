class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newNode):
        new_data = Node(newNode)
        new_data.next = self.head
        self.head = new_data

    def printList(self):
        node = self.head
        while node:
            print(node, end=' ')
            node = node.next

    def removeDuplicate(self):

        track = {}
        current = self.head
        while current:

            if current.data not in track:
                print(current.data, end=' ')
            track[current.data] = True
            current = current.next


llist = LinkedList()
llist.push(1)
llist.push(17)
llist.push(1)
llist.push(2)
llist.push(4)
llist.push(5)
llist.push(17)

print(llist.removeDuplicate())
