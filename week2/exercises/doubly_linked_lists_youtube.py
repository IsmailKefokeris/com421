class node():
    
    def __init__(self, data):
        #Data component = This is an object based on the data passed in
        self.data = data
        #Next component = keeps track of the next pointer to the next node
        self.next = None
        #prev component = keeps track of the next pointer to the next node
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def append(self, data):
        #This will take a piece of data create a node then append(add) it to the end of the list
        #If the head of the list is none run this if statement (if the list is empty)
        if (self.head is None):
            #create a new node using a variable and store the data for the node in it
            new_node = node(data)
            #set the previous to none because this is the first node ever added into the list meaning there is nothing behind it
            new_node.prev = None
            #set the first item (the head) of the list to the new_node variable which was created to store the list data
            self.head = new_node
        #this will run if the list contains 1 or more items
        else:
            #creates a new_node variable to store the list data
            new_node = node(data)
            #creates a current variable which will store the first node in the list (this allows for us to cycle through the list in a while loop)
            current = self.head

            #using a while loop we will cycle the loop until we reach the end 
            while current.next != None:
                #sets the current to the next node in the list until the last
                current = current.next
            #we want the next pointer of the current next node to point to the new node not the end (NONE) because it isnt the end anymore
            current.next = new_node
            #once the loop closes after current.next is equal to None (reached the last item)
            #setting the previous node for our new_node to the current one (meaning the old last item in the list)
            new_node.prev = current
            #setting our new_node to the last item in the list (replacing our current item)
            new_node.next = None

    def prepend(self, data):
        #This will create a node and place it at the front of the linked list
        #The if statement checks if the list is empty (the head is equal to None)
        if (self.head is None):
            #creates a new_node variable to store our node data inside (item data for the list)
            new_node = node(data)
            #that new item in the list sets its previous link to none because its the first item of the list
            new_node.prev = None
            #then it will set itself as the new list head or starting point
            self.head = new_node
        #if the list has already 1 or more items inside then this will run
        else:
            #creates a new_node variable to store our list data the node inside of
            new_node = node(data)
            #the current first item in the list (head) previous will be changed from None to our new_node
            self.head.prev = new_node
            #our next item for our new_node will then link to our current first item making itself the item before the first item (the new first)
            new_node.next = self.head
            #and we can now set officially our new_node as the first item and setting it as the head of the list
            self.head = new_node
            #we also need to make sure its previous is equal to None because it is the first item of the list
            new_node.prev = None

    def verify(self):
        #To verify if the list is working as expected
        #sets the current value as the head (the start of the list)
        current = self.head
        #prints currents data
        print (current.data)
        #creates a loop to print out the full list(while current is not equal to none I.E. not the end of the list keep going)
        while current.next != None:
            #current will continue cycling until it reaches the end
            current = current.next
            #prints currents data
            print (current.data)

list = LinkedList()


list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.prepend(0)

list.verify()
    