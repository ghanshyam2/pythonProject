class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        node = self.head

        while node:
            print(str(node.data), end=' ')
            node = node.next

    def count_element_in_linkedlist(self, search_for):
        current = self.head
        count = 0

        while current:
            if current.data == search_for:
                count += 1
            current = current.next
        return count


list = LinkedList()
list.push(1)
list.push(2)
list.push(3)
list.push(1)
list.push(4)
list.push(1)
print(list.count_element_in_linkedlist(1))
