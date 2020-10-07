
class node():
    #A node needs to contain data 
    def __init__(self, data):
        #the data passed through the __init__ method will get attached to the current node using self.data = data
        self.data = data
        self.prev = None
        self.next = None

    def link(self, otherNode):
        self.next = otherNode
        otherNode.prev = self

    def __str__(self):
        return 


class linkedList():
    def __init__(self, data):
        pass


