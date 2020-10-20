# com421
Work from Data Structures, Algorithms and Mathematics (COM421)

## Week 2

Classes - classes are complex data type which provide a way to define our own custom data structures, for example we could create a stack class which will represent a stack or a linkedlist class to represent a linked list. Classes have two key components:

    Methods. A method is an action that can be performed with a class. For example, with a stack class, we could define push and pop methods. For a linked list, we could define an addNode method, to add a node onto the end of the linked list (and update the reference to the last node).

    Attributes. An attribute is an item of data associated with the class. Last week, we saw that a stack uses an array to store its data. So an attribute of a Stack class could be the underlying array. Likewise, a linked list contains references to the first and last nodes in the list. So these could be attributes of the LinkedList class.

### Objects

Object - an object is an instance of a class. For example Polititian could be a class and the objects of the class would be Donald Trump and Joe Bidan. Objects is a specific example of a data structure.


For example you could define a LinkedList class, and then have one LinkedList object to store students at a university, another to store courses, and on and on.

Stack into a class

```python
class stack:
    # __init__ means: is a method used to initialise objects of the class. When creating a class we need to initialise objects of it in some way. sets the internalArray to a blank array ready to start pushing things onto it
    
    # (self) means: refers to whatever current object is being delt with. when we call a method or create an object we can access that object (the current object) through this self paramiter
    def __init__(self):
        #this bellow is technically an array - the [] creates a python list (it is more flexible than an array) FOR THE EXERCISE WE DONT WANT IT TOO COMPLEX
        self.internalArray = []
    
    def push(self, item):
        #code to add an item into the stack
        
    def pop(self):
        #code to remove an item from the top
        
    def __str__(self):
        return self.internalArray.__str__()

    # __str__ means: This is used if we want to print out the stack (the class), if we create an object and print it by default nothing will happen besides memory printed. to actually have something printed we need to have a __str__ method to define how its printed. when this is printed we want to return to the outside the internalArray of the stack
        
```

## Week 3

#### Queues

A queue works as a FIFO (First in First Out) just like a real-world queue
Tasks in a queue are known as "Jobs" - one of the realworld uses of a queue would be a printer queue

Uses a wrap around function where the next item will start to be added to the front if the back is full. (Needs to keep track of the current indice it's on) Queues are essentially circles that wrap around and around...for instance 0, 1, 2, 3, 4, will wrap around and look like 
                                                        0, 1, 2, 3, 4, 0, 1, 2, 3, 4,