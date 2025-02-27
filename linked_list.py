from os.path import curdir


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # 1. Create a new node
        new_node = Node(value)
        # 2. Iterate over the linked list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        curr_node = self.head
        while curr_node:
            if curr_node.next == self.tail:
                curr_node.next = None
                self.tail = curr_node
            curr_node = curr_node.next
        self.length = self.length - 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return True

    def prepend(self, value):
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        curr_node = self.head
        self.head = self.head.next
        curr_node.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

    def pop_index(self, index):

        # 1. If length of LL is 0 return None
        # 2. If Index is one
        if self.length == 0:
            return None
        if index < 0 or index >= self.length:
            return None
        count = 0
        prev_node = None
        curr_node = self.head
        next_node = self.head.next
        for _ in range(index):
            prev_node = curr_node
            curr_node = curr_node.next
            next_node = curr_node.next
        prev_node.next = next_node
        curr_node.next = None
        curr_node = None
        self.length -= 1
        if index == self.length:
            self.tail = prev_node

    def print(self):
        curr_node = self.head
        while curr_node != None:
            print(f"{curr_node.value}")
            curr_node = curr_node.next

if __name__ == '__main__':
    ll = LinkedList(3)
    ll.append(5)
    ll.append(4)
    ll.append(6)
    ll.append(10)
    ll.append(15)
    ll.append(34)
    ll.print()
    ll.pop_first()
    ll.print()
    ll.pop_index(3)
    ll.print()
    ll.pop_index(4)
    ll.print()
    print(f"Length:{ll.length}")
    ll.append(100)
