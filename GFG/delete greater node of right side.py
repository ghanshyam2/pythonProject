class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
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

    def compute(self, head):
        curr = head
        while curr.next:
            if curr.data < curr.next.data:
                curr.data = curr.next.data
                curr.next = curr.next.next
                curr = head
            else:
                curr = curr.next
        return head


llist = Solution()

print(llist.compute([12,15,10,11,5,6,2,3]))
