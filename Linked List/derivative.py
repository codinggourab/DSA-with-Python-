class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def derive(self):
      
        current = self.head
        while current:
            if current.exponent != 0:
                current.coefficient = current.coefficient * current.exponent
                current.exponent = current.exponent - 1
                current = current.next
            else:
                 # Removing the node if exponent is 0
                if current == self.head:
                    self.head = current.next
                    current = self.head
                elif previous:
                    previous.next = current.next
                    current = previous.next
                else:
                    current = current.next
            if current != self.head:
                previous = current
                if current:
                    current = current.next

    def print_list(self):
        current = self.head
        if current is None:
            print("0")
            return
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end="")
            if current.next:
                print(" + ", end="")
            current = current.next
        print()

# Example usage
poly = LinkedList()
poly.insert(4, 3)
poly.insert(3, 2)
poly.insert(6, 1)
poly.insert(7, 0)

print("Original polynomial:")
poly.print_list()

poly.derive()

print("Derivative of the polynomial:")
poly.print_list()