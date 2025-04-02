class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedlList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def create(self,data):
        q = Node(data)
         
        if self.head == None: 
            self.head = q
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = q
    def display(self):
        p = self.head

        if p == None:
            print("List is empty")
            return
        while p != None:
            print(p.data,end=" -> ")
            p = p.next
        print(None)
    
    def reverseLL(self):
        temp = self.head
        prev = None

        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev
    

obj = LinkedlList()

obj.create(1)
obj.create(3)
obj.create(2)
obj.create(5)
obj.display()
obj.reverseLL()
obj.display()