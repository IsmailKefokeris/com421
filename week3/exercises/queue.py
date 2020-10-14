
class queue():

    def __init__(self, capacity):
        self.internalArray = [None] * capacity
        self.front = 0
        self.end = capacity - 1
        self.back = 0

    def add(self, data):

        if (self.back > self.end and self.front != 0):
            self.back = 0
            self.internalArray[self.back] = data
            self.back += 1
        elif (self.back > self.end and self.front == 0):
            err = "ERROR, Queue is Full Remove an ITEM"
            return err
        else:
            self.internalArray[self.back] = data
            self.back += 1

    def remove(self):

        if (self.back == 0 and self.front == 0):
            err = "ERROR, Queue is Empty"
            return err
        elif (self.front > self.end):
            self.front = 0
            p = self.internalArray[self.front]
            self.internalArray[self.front] = None
            self.front += 1
            return p
        else:
            p = self.internalArray[self.front]

            self.internalArray[self.front] = None
            self.front += 1
            return p

    def __str__(self):
        return self.internalArray.__str__()

        
listter = queue(5)

listter.add(5)
listter.add(3)
listter.add(56)
listter.add(7)
listter.add(99)
listter.add(65)
listter.remove()