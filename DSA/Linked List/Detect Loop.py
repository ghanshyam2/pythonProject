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

    def detectLoop(self):
        fast = self.head
        slow = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return 1
        return 0


llist = Linked()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.push(11)


llist.head.next.next.next.next = llist.head
if llist.detectLoop():
    print("Loop Found")
else:
    print("No Loop")