class Node:
    def __init__(self,data):
        self.data  = data
        self.prev = None
        self.next = None
    
class Dbl_LinkedList:
    def __init__(self):
        self.head = None
    
    def create(self,data):
        q = Node(data)
        
        if self.head is None:
            self.head = q
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = q
            
    def Add_Beg(self,data):
        q = Node(data)
        
        if self.head is None:
            self.head = q
        else:
            temp= self.head
            q.next= self.head
            self.head = q
            
    def Add_End(self,data):
        q = Node(data) 
        if self.head is None:
            self.head = q
        else:
            temp= self.head
            while temp.next is not None:
                temp = temp.next
            q.prev = temp
            temp.next = q
            q.next = None  
            
    def Add_InBw(self,data,key):
         q = Node(data)
         temp = self.head
         while temp:
             if temp.data == key: 
                #  temp = temp.next
                 q.next = temp.next
                 q.prev = temp
                 if temp.next is not None:
                    temp.next.prev = q
                 temp.next = q
                 return
             temp = temp.next
                 
    def Del_InBw(self,key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                if temp == self.head:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
            # If the node is the last node
            elif temp.next is None:
                temp.prev.next = None
            # If the node is in between
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
            return
        temp = temp.next
    def Del_Beg(self):
        if self.head == None:
            print("List is empty")  
        else:
            temp = self.head
            self.head = temp.next 
            
    def Del_End(self):
        if self.head == None:
            print("List is empty")  
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
                   
    def display(self):
        curr = self.head
        if curr is None:
            print("List is empty")
            return
        
        while curr is not None:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")
        
        
obj = Dbl_LinkedList()
obj.create(20)
obj.Add_Beg(30)
obj.Add_Beg(80)
obj.Add_End(100)
obj.Add_InBw(10,30)
# obj.Del_Beg()
# obj.Del_End()
obj.Del_InBw(80)
obj.display()