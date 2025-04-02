class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def create(self, data):
        q = Node(data)
        if self.head is None:
            self.head = q
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = q

    def insertPos(self, data, k):
        p = self.head
        q = Node(data)
        while p is not None:
            if p.data == k:
                q.next = p.next
                p.next = q
                return
            p = p.next
        print(f"Value {k} not found in the list.")

    def delPos(self, k):
        p = self.head
        if p is not None and p.data == k:
            self.head = p.next
            p.next = None
            del p
            return

        prev = None
        while p is not None and p.data != k:
            prev = p
            p = p.next

        if p is None:
            return

        prev.next = p.next
        p.next = None
        del p

    def display(self):
        p = self.head
        if self.head is None:
            print("List is empty")
            return
        while p is not None:
            print(p.data, end=" -> ")
            p = p.next
        print("None")

obj = LL()
while True:
    print("1. Create Linked List")
    print("2. Insert at any position")
    print("3. Delete from any position")
    print("4. Display List")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the data to insert: "))
        obj.create(data)
    elif choice == 2:
        data = int(input("Enter the data to insert: "))
        k = int(input("Enter the value after which to insert: "))
        obj.insertPos(data, k)
    elif choice == 3:
        k = int(input("Enter the value to delete: "))
        obj.delPos(k)
    elif choice == 4:
        print("Linked List elements:")
        obj.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice, please try again.")
