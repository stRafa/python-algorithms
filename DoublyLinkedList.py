class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if (self.head is None):
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return False
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if (self.head is None):
            self.tail = new_node
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return False
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self,index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        after = self.get(index)
        before = after.prev
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        
        temp = self.get(index)
        after = temp.next
        before = temp.prev

        temp.next = None
        temp.prev = None

        after.prev = before
        before.next = after

        self.length -= 1
        return True
        
        


dll = DoublyLinkedList(2)
dll.append(3)
print('\nList:')
dll.print_list()
print('\nList:')

dll.pop()

dll.print_list()
print('\nList:')

dll.prepend(1)


dll.print_list()
print('\nList:')

dll.pop_first()

dll.print_list()
print('\nList:')
dll.append(3)
dll.append(4)
dll.append(5)
dll.prepend(1)
dll.print_list()

dll.set_value(2, 7)

print('\ninsert 3:')
dll.insert(3, 11)
print('\nList:')
dll.print_list()


