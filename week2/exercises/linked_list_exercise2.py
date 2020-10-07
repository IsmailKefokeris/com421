
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

    def add(self, newNode):
        #if the list is empty when you add a node it will automatically be set to the first slot in the list
        if (self.first is None):
            self.first = newNode
        
        #if there is already a node in the first slot then this line will run setting a link between the last node and the current node.
        else:
            self.last.link(newNode)

        #This line of code will add the new node to the last node every time a new node is added (constantly updated last)
        self.last = newNode
    
    def get(self, index):
        pass




