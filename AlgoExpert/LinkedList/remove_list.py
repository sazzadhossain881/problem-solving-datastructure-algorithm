class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        prev = self.head

        while temp.next:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
    
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()    

        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(3)
# my_linked_list.pop()
# my_linked_list.pop_first()
my_linked_list.remove(1)
my_linked_list.print_list()
