
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
        

class LinkedList:
    def __init__(self,length=0):
        self.head = None
        self.tail = None
        self.length = length
    #add to tail
    def get_length(self):
        return self.length

    def add_to_tail(self, value):
        if not self.tail:
            new_tail = Node(value, None)
            self.head= new_tail
            self.tail= new_tail
        else :
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1
    #remove head
    def remove_head(self):
        if not self.head:
            return None
        if self.head is not self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            return current_head.value
   #remove tail 
    def remove_tail(self):
        if not self.head:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        current =  self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value


      