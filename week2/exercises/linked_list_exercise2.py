
class node():
    #A node needs to contain data 
    def __init__(self, data):
        #the data passed through the __init__ method will get attached to the current node using self.data = data
        #A node has three attributes, data = actual data stored, next = linked to next node, prev = linked to previous node
        self.data = data
        self.prev = None
        self.next = None

    def link(self, otherNode):
        self.next = otherNode
        otherNode.prev = self

    def __str__(self):
        return self.data.__str__()


"""
n1 = node("Fred")
n2 = node("tommay")
#printing n1 and n2 showing they are seperate nodes
print (n1)
print (n2)

print ("------Will now print prev and next-------")
#linking n1 (first node) to n2 (Second node) allowing for use to go from one to the other
n1.link(n2)


#proving the link works 
print (n1.prev)
print (n1.next)
print (n2.prev)
print (n2.next)
"""


class linkedList():
    def __init__(self):
        #linked lists need a reference to both the first node (self.first) and the last node (self.last) so we can efficiently add items to the list
        self.first = None
        self.last = None

    def add(self, data):
        #if the list is empty when you add a node it will automatically be set to the first slot in the list
        if (self.first is None):
            newNode = node(data)
            newNode.prev = None
            self.first = newNode
        
        #if there is already a node in the first slot then this line will run setting a link between the last node and the current node.
        else:
            newNode = node(data)

            current = self.first

            while current.next != None:
                current = current.next
            
            self.last.link(current)

        #This line of code will add the new node to the last node every time a new node is added (constantly updated last)
        self.last = newNode
    
    def get(self, index):

        current = self.first
        
        print (current.data)

        while current.next != None:
            current = current.next
            print (current.data)



mylist = linkedList()


mylist.add(1)
mylist.add(3)
mylist.add(5)
mylist.add(4)

print ("at 2nd is: {}".format(mylist.get(2)))


#new attempt at Linked Lists
"""
class node:

    def __init__(self, data = None):
        self.data = data
        self.next = None


class linked_list:
    
    def __init__(self):
        self.head = node()

    def add(self, data):
        new_node = node(data)
        cur = self.head

        while (cur.next != None):
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        
        while (cur.next != None):
            total += 1
            cur = cur.next
        
        return total
    
    def get(self, index):

        if index >= self.length():
            print("ERROR")
            return None
        curindex = 0
        cur_node =self.head

        while True:
            cur_node = cur_node.next
            
            if curindex == index:
                return cur_node.data
            curindex += 1
                
    def display(self):
        elems = []
        cur_node = self.head

        while (cur_node.next != None):
            cur_node = cur_node.next
            elems.append(cur_node.data)

        print (elems)

    def erase(self, index):

        if index >= self.length():
            print ("ERROR")
            return None
        
        curindex = 0
        cur_node =self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next

            if curindex == index:
                last_node.next = cur_node.next
                return 
            curindex += 1

mylist = linked_list()


mylist.add(1)
mylist.add(3)
mylist.add(5)
mylist.add(4)

mylist.display()

print ("Erase Element at 3rd index: {}".format(mylist.erase(3)))

mylist.display()

"""