class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeDuplicate(head):
    if not head:
        return head
    curr = head
    sets = {curr.data}
    while curr.next:
        if curr.next.data in sets:
            curr.next = curr.next.next
        else:
            sets.add(curr.data)
            curr = curr.next
    return head


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


llist = LinkedList()
llist.push(1)
llist.push(17)
llist.push(1)
llist.push(2)
llist.push(4)
llist.push(5)
llist.push(17)

print(removeDuplicate(5))
