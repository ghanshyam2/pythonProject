class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked:
    def __init__(self):
        self.head = None

    def push(self, newNode):
        new_node = Node(newNode)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        node = self.head

        while node:
            print(str(node.data) + "->", end='')
            node = node.next
        # print("NULL")

    def middleList(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("middle of linked list is :-", slow.data)


if __name__ == "__main__":
    list = Linked()

    for i in range(5, 0, -1):
        list.push(i)
        list.printList()
        list.middleList()
