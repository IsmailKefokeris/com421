
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
        self.first = None
        self.last = None

    def add(self, otherNode):

        if (len(linkedList) == 0):
            node(otherNode)
            self.first = otherNode
            
            
        else:
            node(otherNode)
    
    def get(self, index):
        count = 0

        while (count != index):
            count += 1




