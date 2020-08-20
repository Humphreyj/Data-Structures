
class Node:
    def __init__(self, value, next=None):
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
        if self.head == self.tail:
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
        if self.tail is None:
            return None
        elif self.tail == self.head: #case for length == 1
            value = self.tail.get_value() #store the tails value with our get_value method
            self.head = None #set head to none
            self.tail = None #set tail to none
            self.length -= 1
            return value
        else:
            value = self.tail.get_value()
            self.tail = self.tail.get_next()#set the tail to the next value
            self.length -= 1
            return value


      