class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class InsertStart:
    def __init__(self):
        self.head = None
        

    def AddStart(self, data): 
        newNode = Node(data)
        if self.head is None:  # list is empty
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
    def AddLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
    def delBegin(self):
        if self.head == None:
            print("List is empty")
        else:
            self.head = self.head.next
            
    def delLast(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
    def freq(self):
        p = self.head
        f = {}
        
        while p:
            if p.data in f:
                f[p.data] += 1
            else:
                f[p.data] = 1
            p=p.next
        return f
        
        
        
    def display(self):
        curr = self.head
        if curr is None:
            print("List is empty")
            return
        
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Test the Linked List
slist = InsertStart()
slist.AddStart(20)
slist.AddStart(20)
slist.AddStart(10)
slist.AddStart(80) 
slist.AddStart(90)

print("List after adding elements at the start:")
slist.display()

slist.AddLast(100)
slist.AddLast(200)

print("\nList after adding elements at the end:")
slist.display()

print("\nList after deleting first elements:")
slist.delBegin()
slist.display()
print("\nList after deleting last elements:")
slist.delLast()
slist.display()

fr = slist.freq()
print("Frequency is : ",fr)
