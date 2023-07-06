class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        node = self.head

        while node:
            print(str(node.val), end=' ')
            node = node.next
        print()

    def count_node(self):
        result = 0
        curr = self.head

        while curr is not None:
            curr = curr.next
            result += 1
            if curr == self.head:
                break
        return result


if __name__ == "__main__":
    lis = LinkedList()
    for i in range(6, 0, -1):
        lis.push(i)
        lis.printList()
    print(lis.count_node())
