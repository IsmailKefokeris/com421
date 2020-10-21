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


## Week 4

#### Hash Tables

Hash tables allows us to look up values using non-numerical indices or Keys, we might want to implement an address book in which names are the keys and the addresses are the values...another example is student records where the student ID is the key and the full student record is the value.

Looping through a full array to look for an item is inefficient, for instance if there are say 10000 items in an array the searching for an item at 9990 would be super slow. we call this an O(n) operation where n is the index of the item and the performance of the search will depend on the index of the item in the array.

To do better and have a more efficient way of looking up data we can use hash tables. A hash table is an efficient data structure which uses keys (indices) that are converted to a numerical hash code using a mathematical function. This hash code is used to look up items in an array. The has code will be used as the arrays index.


#### Example

simple example for has tables, a simple has function might simply add the ascii codes of the characters making up the key, We might want to use a dictionary program storing words as the keys and their meanings as the values.

    e.g for the key "cat" - summing the ASCII codes gives 99+97+116 = 312 -For the key "dog" - we get 100 + 111 + 103 = 314
    For the key "rat" - we get 114 + 97 + 116 = 327

The has code returned from the hash function can then be used as the array index. We would place the key/value pair "cat" and "Furry animal which goes meo" at index 312 and the underlying array. "dog" would be 314 and "rat" would be 327

#### Problem:

If we enter "act" we will have a problem, the hash function for "act" would be 97+99+116 which equals 312 which is the same as "cat"...clashing, there are two common solutions to clashing, separate chaining and linear probing.

#### Separate Chaining

In separate chaining the array will contain buckets. each item will be given a hash code and placed into the bucket for the hash code. One bucket can contain more than one item.... for instance "cat" and "act" would be placed in the same bucket due to them having he same hash code.. Each bucket would contain a list of items at each entry of the array.

#### Linear Probing

Linear probing is an alternative approach where each array index contains only one item (Not a list). If there is a clash the item is movbed on to *The next available place in the array" so in the example above, "cat" and "act" would have a hash code of 312. Since "act" is the second item to be added it will then be moved from 312 to 313 giving it its own position.

#### Secondary Hash Function

To minimise cluster in linear probing you can use this function to calculate displacement and increase the number of places in the array. 
for example if the secondary hash function gives 7 for "act" we would place "act" at 312 + 7 = 319
    Secondary hash functions typically involve a modulo calculation for example:
                        (secondaryHash = sumOfAsciiCodes % N)

"s" is our string.
"s[0]" = the ascii code of position 0 in the string
"s[1]" = the ascii code of position 1 in the string
power off = ** in python
f = a number (anything) normally prime number...

s[0]*f^0 + s[1]*f^1 + ... + s[n-1]*(f^(n-1))


f = 10

"cat" vs "act"

99, 97, 116 (cat ascii)

(31 is the best number to use...prime number)
(10 would be replaced with 31...So 99*31^0...etc)

"cat" 99*10^0 + 97*10^1 + 116*10^2 = 99*1 + 99*10 + 116*100 = 99 + 970 + 11600 = 12669

97, 99, 116 (act ascii)

"act" 97*10^0 + 99*10^1 + 116*10^2 = 97*1 + 99*10 + 116*100 = 97 + 990 + 11600 = 12687

Our array should be a prime number, if for instance you are storing student data for around 100 students..to minimise clashes you want to give your array a capacity greater than the number of records you are likely to store (127).now we can do a modular calculation on the hash table...

(Some say make your underline array twice as big as the maximum number of items you will need to store you should minimise clashes)

12669 % 127 = 96 (thats the bucket that the item will go into) "cat"

12687 % 127 = 114 (thats the bucket that the item will go into) "act"


#### Why use a prime array size?

If our hash codes are truly random there wont be a need for a prime bucket size..the problem is in certain cases we will want to store the data numerically related.. for example memory addresses are often multiples of 4 because of how data is stored...so if we want to calculate a hash code for a variable based on memory address it means all our hash codes will be a multiple of 4 which will be a poor choice because clashes will be very likely... All buckets which are multiples of 4 will fill up but all the other buckets will stay empty. This can be generalised: if the hash codes end up being multiples of some number n, then choosing a hash code which is also n or a multiple of n will end up with more clashes than expected by chance. its better to choose a prime number to avoid this... and even if hash codes are not related in any way its a good practice.


#### Implementation details









