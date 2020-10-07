

class Stack:
    def __init__(self):
        self.internalArray = []

    def push(self, item):
        # Code to add an item to the stack
        self.internalArray.append(item)

    def pop(self):
        #checks if the stack is empty or not (can also be used to determan if the stack is at max capacity if needed)
        if (len(self.internalArray) == 0):
            return "EMPTY"
        else:
            #store top of stack into a variable
            p = self.internalArray[-1]
            #remove the top item in the stack
            del self.internalArray[-1]
            #return the top item which was removed (and saved in a varaible)
            return p
    
    def peak(self):
        #Checks if the stack is empty before allowing a peak
        if (len(self.internalArray) == 0):
            return "EMPTY"
        else:
            # returns the top most item in the stack
            return self.internalArray[-1]

    def __str__(self):
        return self.internalArray.__str__()

#defining a stack
stack1 = Stack()

#pushing items into a stack
stack1.push("linux")
stack1.push("windowies")
stack1.push("maccy")

#printing the full stack
print("Full stack", stack1)

#example of peaking a stack to see the top most item
peak1 = stack1.peak()
print("peak1", peak1)
#example of popping (removing) an item from a stack
popped1 = stack1.pop()
print("popped", popped1)
#example of popping (removing) an item from a stack
popped2 = stack1.pop()
print("popped", popped2)
#example of popping (removing) an item from a stack
popped3 = stack1.pop()
print("popped", popped3)
#example of popping (removing) an item from a stack when there are no items left in the stack (observe response)
popped4 = stack1.pop()
print(popped4)

#printing the stack after all modifications
print("full stack", stack1)