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

N/A



## Week 5

#### Trees

A Tree is similar to a real tree but in reverse...The Root would be at the top and the child notes would be connected downwards from the root. A tree is a sequence of nodes.

Used when we need to arrange data hierarchically we would use trees. for instance html, the page body is the root node and the child nodes would be the headers or paragraphs.. Trees can also be used to do efficient searching and sorting of data...or the use with a scene graph.. Used in graphical application (games) so 3D objects for instance a horse might have a rider object where the rider would be the decendant of the horse because he is attatched to the horse (the rider is a child node) so if the horse moves the rider will move together with its parent (the horse)

#### Binary Trees

Binary tree is a form of a tree where each node will have only two child nodes, a left and right node..
This makes them useful for sorting data for instance.

This is probably best illustrated by example. Imagine you want to sort the numbers 29, (20), (17), 40, 25, (18), 1. How might you do that with a binary tree?

- You put the first number (i.e. 29) in the root node of the tree
- The next number ((20)) so we compare it to the parent node since its less than (29) it will be placed as the left child node
- Now ((17)) is less than (29) so we will go to the left node but that is occupied with (20) so we will go down another level and compare (17) with ((20)) and since ((17)) is less than ((20)) it will be added to the left node of ((20)).
- The fourth number (40) is bigger than 29 which means it will get placed to the right child node (of 29)..
- The next is (25) which is less than 29 so we put it on the left but (20) is there so it will compare 25 with (20) and 25 is bigger than (20) so 25 will get placed on the right as the right child node.
-The next number is (18) which is less than 29 so it goes to the left node to (20)..its also less than (20) so it goes to the left of (20) where (17) is but (18) is bigger than (17) so we add (18) to the right node of ((17)).
- The last is 1 so itll go all the way down to (17) and is added as the left node of (17).

#### Exercise
On paper, create a binary tree containing these numbers in order:

                                                    8934 9 843 1 83 23 389

![Binary Trees](picture/Binarytrees.png "Binary Trees")

#### Retrieving data in sorted order

Start at the root node.
Descend to the left child node.
If it has child nodes of its own:
    first descend its left child node and print out the value within;
    print out the value within this node;
    then descend its right child node and print out the value within.
If it does not have child nodes of its own, simply display the value within.

Repeat the process with the right child node of the root.

What do we do if the left child node's own left child node also has child nodes? We simply repeat the process and keep going until we finally hit a node with no child nodes of its own.

![Binary Trees](picture/treeexample.png "Binary Trees")

The 29 node has two child nodes, 20 and 40, so we descend to 20 first.
The 20 node has two child nodes, 17 and 25, so we descend to 17 first.
The 17 node has two child nodes, 1 and 18, so we descend to 1 first.
1 has no child nodes, so we just print out 1 and ascend to its parent (the node containing 17)
Having dealt with the left child of the node containing 17, we print out the value itself (17) first, then descend to the right node (18)
The 18 node has no child nodes, so we just print out 18
We then ascend back to the 17 node. The 18 node was the right node of the 17 node, so we are done processing this branch of the tree. So we go back up again to the 20 node.

We have dealt with the left branch of the 20 node, but not the right. This means we first print out the value, 20 and then descend the right node.

The right node of 20 contains a value, 25, but no child nodes of its own so we just print out the value (25)
We then ascend back to the parent, 20, as we are done with this branch.
We have also covered all branches of 20, so we ascend back up to the root node, 29.
We have dealt with the left branch of the 29 node, but not the right. This means we first print out the value, 29 and then descend the right node.

The right node of 29 contains a value, 40, but no child nodes of its own so we just print out the value (40)
We then ascend back to the parent, 29, as we are done with this branch.

We have now covered the left branch, the value, and the right branch of the root node. This means we are done with the tree. If you track back the order in which the values were printed, you'll find they are in order:

                                                            1 17 18 20 25 29 40


#### Recursion

Recursion is the process of a function calling itself over and over again until a condition is met...for instanec this is some code to print out the numbers 1 to 10 using recursion.

```python
def recursive_print (value, max_value):
    print(value)
    if value < max_value:
        value += 1
        recursive_print(value, max_value)

recursive_print (1, 10)
```

#### Using recursion on a binary tree (Algorithm)

- Starts at the Root node:
        Descends left branch (recursive function)
        Print the value in the node.
        Descend the right branch (recursive function)
- For each node we get to (for example the immediate child nodes of the root node), perform the first three steps again:
        Descend the left branch, if it exists
        Print the value in the node.
        Descend the right branch, if it exists


## Week 7

#### Algorithm efficiency: the "Big O" notation

In algorithms we need to measure how comples an algorithm is (efficiency)..Complexity can be measured in many ways such as performance (time taken) or the usage of memory... The standards for measuring algorithm complexity we use The Big O notion... This expresses complexity in relation to some property (the data we are dealing with) "n"... n is often the size of data (the amount of data) for exampel a list n would be the amount of items in the list (The longer the list the slower or more complex the algorithm would be )... With algorithm efficiency we have to consider worst case senarios

Big O notation is expressed in terms of this property "n"...For Example:
    O(1): if an algorithm is O(1) it means that its complexity is independent of n. Calculating the memory address of the index of an array     would be an example of an O(1) operation because it is always given by the equation:
    
```python
memory_address = start_memory_address + index * bytes_used_by_one_item
```

    Clearly the time taken to evaluate this equation does not depend on the size of the list, which is the property n in this case. Even if the list is very large, and the index is very large, we can quickly calculate the item's address using the simple equation above. O(1) algorithms are thus highly efficient… but not many algorithms are O(1)!

    O(n):  If an algorithm is O(n) it simply means that the complexity depends on the value of "n"(Directly or linearly)...If n was increased by 2 the complexity will also increase by another 2...for example linked lists is an O(n) algorithm because we will have to manually follow the links to retrieve the item in the list with a specific index...we cannot rely on memory addresses...

The Worst-case scenario is simply that we assume the index would not be found until the end of the list where n is the number of items in the list..

    O(n^2): (^Indicates a power) when na algorithm is O(n^2) then it means the time takne or memory used will be influenced by the square of the number of items...So if the number of the items doubles then the time taken will increase around four times or if the number is increased by 10 this means the time taken will be increased by 100 times

Algorithms in which we have an outer and inner loop which will loop through the array twice would be an O(n^2) algorithm..the outer loop will be run "n" times and the inner loop will be run "n" times...For example an outer and inner loop. A function do_something() is performed n^2 times (16 times in the example, as n is 4). If n is changed to 5, then the operation will be performed 25 (5^2) times.

```python
n = 4
for i in range (n):
    for j in range (n):
        do_something(i, j)
```
As can be seen this is not very efficient..

Big O notation is used to classify algorithms...so we have O(n^2) but we dont have and never will O(n^2) + 1 for complexity...Even if the time taken would be n^2 + 1 we wouldnt show it as that but instead as O(n^2).

Any compelxity equation that has n^2 in the equation means they can be approximated (simplified) simply to O(n^2)...


The diagram below shows how complexity increases with increasing n for different classes of Big O complexity:

    n is along the x (horizontal) axis, while the complexity is along the y (vertical) axis;
    green is O(n);
    red is O(n^2);
    blue is O(log n); to be discussed below;

    magenta is the quadratic equation 0.5*n^2 + 0.5n. This shows that the quadratic form is exhibited, and the shape of the graph, with a rapid increase with the rate of increase getting bigger with larger values of n is very similar to n^2. (This is known as a parabolic graph). So, even if the complexity is not exactly O(n^2), the behaviour of the graph for increasing n is essentially the same as O(n^2).


![Parabolic Graph - NickWhitelegg](picture\download.png "Parabolic Graph") This is known as a Parabolic Graph...



    O(log n): When algorithms are O(log n) O is related to the log of n...Logarithm is the inverse operation of a power...A log of a number (relative to a particular base, such as base 10 or base 2) will give you the power the base has to be raised to to equal that number...so if b to the power of p is x then log(b)x = p....(log explained)


    b^p = x ----> log(b) x = p

From this we can see that the O(log n) operation is far more efficient because we can increase n significantly but the consumed time or memory will not increase too significantly... For example if we were to use it on a list of 256 (2^8) items it will only take twice as long as a list of 16 (2*4) ...compared with that of a O(n) algorithm which will take 16 times longer because 16 x 16 is 256....


#### Sorting Algorithms...

##### Bubble Sort

Bubble sort is a simple algorithm but not very efficient....You go through a list of values and consider pairs at a time..

![Bubble Sorts - NickWhitelegg](picture\bubble-sort.png "Bubble Sorts")




##### Swapping variables over

to swap variables you would need to create a temp variable...

```python
tempVar = a # Stores the Original value of A
a = b # A contains original value of B
b = tempVar # B takes the original value of A

# we cannot just...

a = b
b = a
```

#### Selection Sort

Selection Sort is a different type of sorting algorithm and is conceptually simple but (relatively) inefficient...It does have its advantages over bubble sort for example the number of swap operations is minimised (It is O(n) rather than O(n^2))....

![Diagram by Brian Dupee sourced from sorting-algorithms.com](picture\selection_sort.png "selection_sort")

Selection sort involves going through the list and for each member of the list finding the lowest member of the list and swaping with current if current is greater than that value...we go through the list and compare the current with the lower one...

When swapping numbers swapping may not be computationally expensive however if the two values are more complex objects which takes time to initialise then the fact that we need to create a temp varuable can mean a swap will be expensive...in cases like this selection sort is particularly favoured over bubble sort.


#### Insertion Sort

Another type of simple sort which has the complexity of O(n^2) in most cases but can also occasionally be a O(n)....

![insertion_sort - NickWhitelegg](picture\insertion_sort.png "insertion_sort")

WE start with the first value...then we move to the second value, we then check if there are any members in the sorted part of the list(the part before the devider (the red box)) are less...we compare the current item with the list before the current item that is greater than the current item....

A great advantage of insertion sort is that if you do know that some of the data is already sorted you are able to avoid the use of an innerloop...if the divider value is greater than the one immediately to the left then we wont need to use an innerloop instead filter it through an If statement...

            (Note that we can perform a useful "trick" here which can prevent us having to do the inner loop at all. If the last value of the sorted part of the list - which will be the value immediately to the left (i.e one index below) the "divider", is less than the "divider", then we know that the "divider" is already in its correct position. This is because the sorted part of the list is sorted, and the highest value within the sorted part will be immediately to the left of the "divider". So if the "divider" is greater than this value, we do not to move it. Thus, we do not need an inner loop.) 
                                                --- Said better than i explained probably...


#### Week 8 - Efficient Searching Algorithms

WE want to avoid brute force algorithms when searching...a brute force algorithm doesnt really implement intelligence...For instance if we search through a list and compare each item in the list with the item we want it would be very slow and be known as a brute force algorithm...

another example of brute force is trying to find a factor of a number...for example the factore of 24 is 2, 3, 4, 6, 8, and 12 a brute force way would be to loop through all numbers and dividing those numbers to see if they give us an integer meaning its a factor...Again testing every single integer...

##### Binary Search

Binary search is a more efficient way of searching compared to a brute force search (called linear search)...It is a O(log n) complexity...which we say last week it is better than O(n)...Binary Searches work by repearedly guessing a position to index in a list to find the item(data) required...To use Binary Search we must have the list sorted using a sorting algorithm first....This can be used in things such as searching for a record in a large list of people in a system of sort...(student records system) its likely that searching will have to be done many many times but by contrast the data would only have to be sorted once when the daata is first created or at worst when a new record is added to the data which is less likely to happen....

Binary Search is known as divide and conquer algorithm...
Here is an example of binary search. We have an array with 100 members containing names sorted in alphabetical order, and we are searching for "Smith, Tim".

First we select the midpoint of the list, this could be the member with index 49 or 50 doesnt really matter which for a 100 member list... (in python)
```python
math.floor((start + end) / 2) # need to import math

```

start is the start part of the list we are searching... and end si the end part of the list (99 assuming its a 100 list)....(note math.floor takes a floating point number and rounds it down...)...if the length is an even number (100) it will give us the index of the item immediately before the midpoint (49) while if it is an odd number (101) it will give us the exact midpoint (because indices start from 0 and math.floor(101/2 is math.floor(50.5))) which is 50...exactly halfway between 0 and 100

SO once we select our midpoint in this case 49....So, say we find "Jones, Jane" at position 49 in our example. We know we need to look within the range 50-99 because "Smith, Tim" is after "Jones, Jane" in the alphabet. So we repeat the divide-and-conquer operation. We find the midpoint of 50 and 99 (74) and look at the value there. It's "Nodd, Nigel".

We repeat the process. "Smith, Tim" is after "Nodd, Nigel" in the alphabet so we know we have to search the portion of the list after 74. So we find the midpoint of 75 and 99, which is 87. We might get "Trott, Tina" at this position, so now we need to look at the portion before 87 (as "Smith, Tim" is before "Trott, Tina" in the alphabet). So we have to search within the portion75-86. We choose the midpoint, 80, and now found "Raven, Roger".

Our area of search is cut down now to 81-86. We pick 83 and find "Smith, Alice", i.e just before "Smith, Tim" alphabetically. We then only have three list positions to search - 84 to 86. So we pick the midpoint 85. We find "Smith, Simon". We now only have one possibility - 86 - and looking at item 86 we finally find what we want, "Smith, Tim".

The diagram below shows the process. Our search term (Smith, Tim) is shown using a red circle.

![Binary Search - NickWhitelegg](https://nwcourses.github.io/COM421/images/binary_search.png "insertion_sort")


#### Assignment Info

Should not search by name in question 2 must be something else - Give each point a unique key for example

question 6 - use queues for enquiries..


#### Week 9 - More Advanced Sorting Algorithms

These algorithms use recursion... (Quick sort and Merge Sort)

Quicksort - Works by recursively partitioning the list into two sections or partitions...the sides of an element are known as a pivot.
A pivot is the central item...

We first pick the pivot (often the last value or the first or the middle - this is arbitrary)
Then we partition the values (into two partitions) into those lower than the pivot and those higher
We then repeat it recursively with each section (lower than pivot and higher than pivot) to finally sort them

To work out which element is less than or greater than the pivot we will be using the Hoare Partitioning Algorithm...

##### The Hoare partitioning algorithm

The hoare Algorithm was developed from Tony Hoare, it works by having two "fingers" pointing to the start of the list and the end of the list...we will first move the first "finger" which is referenced by the variable i forwards and the second "finger" referenced by the variable j backwards....until i points to somethign greater than or equal to the pivot and j points to something less than or equal to the pivot.

![Hoare Algorithm Quicksort - NickWhitelegg](https://nwcourses.github.io/COM421/images/qsort2.png "Quicksort")

Afterwards the quicksort function will then... get a new pivot by calling the hoare partitioning algorithm,..recursively calls quicksort on the section left of the pivot and right of the pivot...

Pseudo Code:

```python
function hoare_partition(data, start, end)
    Let i = start
    Let j = end
    Let pivot = midpoint of list # this is arbitrary

    While true # this will loop forever

        Increase i until we find a number equal to or greater than number at pivot position
        Decrease j until we find a number equal to or less than number at pivot position

        # At this point, the numbers pointed to by i and j will be in the 'wrong' 
        # part of the list, so swap them, unless i and j are equal or have crossed over, 
        # in which case we have finished this run

        If i and j haven't crossed over yet, swap the numbers
        If i is less than j
            Swap the numbers
        else
            return j  # i and j have crossed over. Use j as the new pivot - could also use i
```

apart from this we will need a master function...this function will take in as parameters the list, the partition start index, and the partition end index.... first thing we check in master function is if end is > than start index...otherwise 
            uses Hoare partitioning to partition the list and find a pivot
            recursively call the "master" function passing in the partition before the pivot
            recursively call the "master" function passing in the partition after the pivot

#### Week 10 Path-Finding

Key thing is we use a datastructure known as a graph in pathfinding... a graph is a datastructure which shows the connection between a particular point called nodes...A node is a point of interest(could be a city town village pub or restauranet or what ever even road junctions) connections between nodes(lines) are known as edges, in graphs we show nodes and lines between the nodes, nodes store the info in them as class this includes the name of the place and all the edges leading from the singular node...The edge class stores starting node and the ending node aswell as some info about the edge such as the distance. 


![graph for pathfinding - NickWhitelegg](https://nwcourses.github.io/COM421/images/railgraph.png "graph")


More generally in graphs edges may store somethign called weight(which is known as cost) the cost for going on that route, for example if calculating a route by bike you might want to avoid steep hills which is a feature and if it is steep then the weight for the edge will be increased (shortest route is 4km but has a steep hill so the weight would be distance multiply the cost (maybe 1.5) so itll be 5.5 longer and there may be a better route)

This is all known as a topology

##### Dijkstra's Algorithm

This algorithm is used to find a route from one node to another....This is a way of efficiently routing from one node to another, we start at a starting node(london) and we gradually explore node by node until we reach the end node(munich) This works  by keeping track of something called an open list, a list of nodes we have explored but havent considered, Consider means we are on that node and looking at all edges from that node (explore) so while we havent considered it we wont know what connects to it.

first step explore neighbours, brussels and paris so we add the two to the open list,

we store the distances from london in the node, we know that the edge from london to brussels is 370 so we store it into the brussels node which is shortest so far. we do the same with paris and we remove london from the open list, 

we then select the node from the open list with the lowest distance to explore (in this case brussels at 370) we will now consider brussels and expand out to Amsterdam and Cologne and we add them both to the open list and store 581 to the nodes which is (london to brussels plus brussels to the next city in this case the same distance regardless of amsterdam and Cologne)

We dont go to paris from brussels because the distance will be longer than just going from london to paris rather than london to brussels then to paris.

Note amsterdan and cologne have a longer distance than from london to paris, so we will now have to explore paris, notice nodes we have considered are white and ones we still need to are yellow.

neighbours of Paris would be brussels (which we can ignore ) and go to the others which are frankfurt(1033) and stuttgart(1085) which are the values added all up and they are added to the open list now. we now have considered paris so paris is off the open list

we will now consider amstardam because again shortest distance, amstardam has no new neighbours (because of brussels and cologne) and we dont need to move because the route to cologne via amsterdam is longer than to brussels...so nothing is needed to happen here.

we are now on Cologne which has one new neighbour which is frankfurt and it combines its distances together(771) its already on the open list so we wont need to visit it again the distance from london to frankfurt via cologne is shorter than paris to frankfurt and since its less we can update the frankfurt distance from 1033 to 771, when we explore a node we set its parents(links between current node and previous node) to the preceeding node (parent of frankfurt was originally Paris but now itll be set to Cologne because distance is shorter)

since frankfurt is shortest itll be the next current node, it has two neighbours stuttgart(978) and munich, the same happens with stuttgart that happened with frankfurt meaning we can update it but we also find the route which was needed to munich (1164) Even though we have found munich it is still possible there is a shorter route (even though we know there isnt the computer doesnt)

So finally we explore stuttgart and check distances, if it is shorter it would update but it isnt (because it is 978 + 221 = 1199) so that is where it ends.

![Dijkstra's Algorithm - NickWhitelegg](https://nwcourses.github.io/COM421/images/dijkstra2.png "Dijkstra's Algorithm")

Nodes considered/ visited can have a boolean message inside saying it has already been explored and doesnt need to go again

WE can use deque for the list to get the correct order, with deque we start with the end and move backwards to the start.

##### Implementing a priority queue in Python

A priority queue allows for items to be added and sorted based on a numerical value given to the item, this is perfect because our value can be distance

to use it we need to import the module "heapq". priority queues are implemented using a specific type of sorted tree which is known as a heap...Heap is a tree where every parent node will have a value which is less than or equal to any of its children...A simple example of creating a priority queue and then removing items from it...Note we use heappush() to add to the queue and heappop() to remove from the front of it

```python

import heapq
from heapq import heappush, heappop

# Create an empty list. This will be converted to a heap.
h = []

# Add tuples containing a numerical value and another item of data (place name here) to the priority queue. If tuples are added, the queue will be prioritised using the first item in the tuple.
heappush (h, (461, 'Paris'))
heappush (h, (370, 'Brussels'))
heappush (h, (1164, 'Munich'))
heappush (h, (771, 'Frankfurt'))

# Remove each item one by one from the priority queue until it's empty.
while len(h) > 0:
    hp = heappop(h)
    print(hp)

```


