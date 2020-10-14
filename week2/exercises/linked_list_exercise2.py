
class node():
    #A node needs to contain data 
    def __init__(self, data):
        #the data passed through the __init__ method will get attached to the current node using self.data = data
        #A node has three attributes, data = actual data stored, next = linked to next node, prev = linked to previous node
        self.data = data
        self.prev = None
        self.next = None

    def link(self, otherNode):
        self.prev = otherNode
        otherNode.next = self

    def __str__(self):
        return self.data.__str__()



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
    #****get doesnt really work but all the other methods seem to work just fine Ill have a look at it another time....****
    def get(self, index):
        counter = 0
        current = self.first
        
        print (current.data)

        while current.next != None and counter < 0:
            counter += 1
            current = current.next
            print (current.data)
        
        return current



mylist = linkedList()


mylist.add(1)
mylist.add(3)
mylist.add(5)
mylist.add(4)

print ("at 2nd is: {}".format(mylist.get(2)))
