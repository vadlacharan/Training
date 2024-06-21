class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_back(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            new_node.prev = temp
            temp.next = new_node
            self.tail = new_node

    def add_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def reverse_display(self):
        temp = self.tail
        while(temp!=None):
            print(temp.data)
            temp = temp.prev

    def traverse(self):
        temp = self.head
        while(temp != None): 
            print(temp.data,end="->")
            temp = temp.next
    
    def even_odd(self):
        t1 = self.head
        t2 = self.tail
        while(t1 != None or t2 != None):
            if t1 == t2:
                return "odd"
            t1 = t1.next
            t2 = t2.prev
        return "even"

    def palindrome(self):
        t1 = self.head
        t2 = self.tail

        while( t1 != t2 ):
            if( t1.data != t2.data):
                return "Not a Palindrome"
            t1 = t1.next
            t2 = t2.prev
        return " it is a palindrome"

    def pattern(self):
        t1 = self.head
        t2 = self.tail

        while( t1 != t2 and t2.next!= t1):
            t1 = t1.next
            t2 = t2.prev
        t2=t2.prev
        t3 = self.head
        temp = 0
        while(t2 != None):
            temp = t3.data
            t3.data = t2.data
            t2.data = temp
            t2 = t2.next
            t3 = t3.next

            



x = LinkedList()
x.add_back(3)
x.add_back(5)
x.add_back(7)
x.add_back(8)
x.add_back(9)
x.add_back(10)
x.add_back(12)
x.add_back(15)



x.reverse_display()
print(x.even_odd())
print(x.palindrome())
x.pattern()
x.traverse() 