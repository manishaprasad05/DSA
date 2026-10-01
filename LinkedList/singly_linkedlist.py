# Singly Linked List
# Node: data, next, head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next

    def user_input(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = input("Enter data: ")
            self.insert(data)


s1 = SLL()

s1.user_input()

print("\nSingly Linked List:")
s1.display()
