class ListNode:
    """Each ListNode holds a reference to its previous node
    as well as its next node in the List.
    """
    def __init__(self, value, prev=None, next=None): # method initializer constructor
        self.prev = prev # set the previous
        self.value = value # set the value
        self.next = next # set the next

    def delete(self): # method to delete
        if self.prev: # if previous
            self.prev.next = self.next # set previous next node as the next node
        if self.next: # if next
            self.next.prev = self.prev # set next previous node as the previous node

class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes.
    """
    def __init__(self, node=None): # method initializer constructor
        self.head = node # set the node as the head node
        self.tail = node # set the node as the tail node
        self.length = 1 if node is not None else 0 # set length to 1 if not None, else 0

    def __len__(self): # method to return length
        """Returns the length of the list"""
        return self.length

    def add_to_head(self, value): # method to add node to head
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly.
        """
        # wrap given value in a ListNode with its 'next' pointing to the current head
        new_node = ListNode(value, next=self.head) # create the new node with next as head node
        self.length += 1 # add 1 to get_length

        if self.head is None and self.tail is None: # if empty
            self.head = new_node # set new node as the head
            self.tail = new_node # set new node as the tail
        else:
            self.head.prev = new_node # set the previous head to the new node
            self.head = new_node # set the new node as the head


    def remove_from_head(self): # method to remove node from head
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        """
        self.length -= 1 # remove 1 from length

        if self.head is None and self.tail is None: # if empty
            return None

        else:
            old = self.head.value # store old head value

            if self.head == self.tail: # if length is 1
                self.head = None # set head to None
                self.tail = None # set tail to None

            else:
                self.head = self.head.next # set the next head value as the new head
            return old

    def add_to_tail(self, value): # method to add a node to the tail
        """Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly.
        """
        # wrap given value in a ListNode with its 'prev' pointing to the current tail
        new_node = ListNode(value, prev=self.tail) # create the new node with previous as tail nodet
        self.length += 1 # remove 1 from length

        if self.head is None and self.tail is None: # if empty
            self.head = new_node # set new_node as the head
            self.tail = new_node # set the new_node as the tail

        else:
            self.tail.next = new_node # set the tail next node to the new_node
            self.tail = new_node # set the tail as the new_node

    def remove_from_tail(self): # method to remove node from the tail
        """Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
        self.length -= 1 # remove 1 from length
        if self.head is None and self.tail is None: # if empty
            return

        else:
            old = self.tail.value # store old tail value

            if self.head == self.tail: # if length is 1
                self.head = None # set head node to None
                self.tail = None# set tail node to None

            else:
                self.tail = self.tail.prev # set tail node as the tail previous node
            return old

    def move_to_front(self, node): # method to move node to front'head'
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List.
        """
        input_node = node.value # store input_node value
        if node == self.head: # if input_node is head
            return

        elif node == self.tail: # if the input_node is tail
            self.remove_from_tail() # use remove_from_tail method, removes node and decreases length

        else: # all else
            node.delete() # use delete method, deletes but does not decrease length
            self.length -= 1 # remove 1 from length

        self.add_to_head(input_node) # use the add_to_head method, add the input_node as the head node

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node): # method to move node to end'tail'
        input_node = node.value # store input_node value

        if node == self.tail: # if the input_node is tail
            return None

        elif node == self.head: # if the node is the head
            self.remove_from_head() # use remove_from_head method, removes node and decreases length

        else: # all else
            node.delete() # use delete method, removes node but does not decrease length
            self.length -= 1 # remove 1 from length

        self.add_to_tail(input_node) # use the add_to_tail method, add the input_node as the tail node

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node): # method to delete a node
        if not self.head and not self.tail: # if empty
            return

        self.length -= 1 # remove 1 from length
        if self.head == self.tail:
            self.head = None # set head to Node
            self.tail = None # set tail to Node

        if self.tail == node: # if the node is the tail
            self.tail = self.tail.prev # set the tail as the tail previous node

        elif self.head == node: # if the node is the head
            self.head = self.head.next # set the head as the head next node
        node.delete() # use delete method, removes node but does not decrease length

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if self.head is None: # if empty
            return

        cur = self.head # set cur as head vlue
        max = cur.value # set max to the cur value

        while cur: # iterate with while loop
            if cur.value > max: # if larger than max
                max = cur.value # max is now the cur value 'max'

            cur = cur.next # check the next value
        return max