# # creating a linked list node.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
 
#     # A function that will reverse the linked list
#     def reverseList(self):
#         previous = None
#         current = self.head

#         # traversing the list till the end.
#         while(current is not None):
#             # making a pointer point to the next node of the current node.
#             next = current.next
#             current.next = previous

#             # making the previous node point to the current node
#             previous = current

#             # moving the current node
#             current = next

#         # setting the head to the reversed list.
#         self.head = previous
 
#     # Function to insert a new node.
#     def insertNode(self, data):
#         newNode = Node(data)
#         newNode.next = self.head
#         self.head = newNode

#     # a function that will check if the linked list is a palindrome linked list or not.
#     def checkPalindrome(self):
#         # base case.
#         if self.head == None:
#             return True

#         a = []
#         # using the pointer to traverse the lists.
#         first = self.head
#         while first != None:
#             a.append(first.data)
#             first = first.next

#         # the first pointer will now point to the head of the reversed list.
#         self.reverseList()
#         first = self.head

#         i = 0
#         # traversing both the list and array and checking each node.
#         while first != None:
#             if first.data != a[i]:
#                 return False
#             first = first.next
#             i += 1

#         return True



# if __name__ == '__main__':
#     # a list containing the data of the linked list.
#     data = [1, 2, 4 , 2, 5]

#     # points to the head node of the linked list
#     linkedList = LinkedList()

#     # constructing the linked list from last to first
#     for i in reversed(range(len(data))):
#         linkedList.insertNode(data[i])

#     if linkedList.checkPalindrome():
#         print("The linked list is a palindrome linked list.")
#     else:
#         print("The linked list is not a palindrome linked list.")


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def create(self,data):
        q = Node(data)
         
        if self.head == None: 
            self.head = q
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = q

    def reverse(self,head):
        prev = None
        temp = head

        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def palindrome(self):
        if self.head == None or self.head.next == None:
             return True
        
        slow = self.head
        fast = self.head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        new_head = self.reverse(slow.next)

        first = self.head
        seconed = new_head
        is_pali = True

        while seconed != None:

            if first.data != seconed.data:
                is_pali = False
                break
            
            first = first.next
            seconed = seconed.next

        slow.next = self.reverse(new_head) # restore original list
        return is_pali

        
    

obj = linkedlist()

obj.create(8)
obj.create(5)
obj.create(1)
obj.create(9)

if obj.palindrome():
        
        print("The linked list is a palindrome linked list.")
else:
        
        print("The linked list is not a palindrome linked list.")


    



