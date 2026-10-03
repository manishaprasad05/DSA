#Singly Linkedlist with switchcase
#Node: data,next,head

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

        if temp is None:
            print("List is empty")
            return

        while temp is not None:
            print(temp.data)
            temp = temp.next


s1 = SLL()

while True:
    print("\n--- Choose ---")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            data = int(input("Enter data: "))
            s1.insert(data)
            print("Inserted successfully..")

        case 2:
            print("\nLinked List:")
            s1.display()

        case 3:
            print("Exited..")
            break

        case _:
            print("Invalid choice")
            data = input("Enter data: ")
            self.insert(data)

