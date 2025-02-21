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

    def pop_index(self, index):

        # 1. If length of LL is 0 return None
        # 2. If Index is one
        if self.length == 0:
            return None
        count = 0
        curr_node = self.head
        next_node = self.head.next
        while count < self.length:
            if count == index:
                curr_node = next_node
            else:






    def print(self):
        curr_node = self.head
        while curr_node != None:
            print(f"{curr_node.value}")
            curr_node = curr_node.next

if __name__ == '__main__':
    ll = LinkedList(3)
    ll.append(5)
