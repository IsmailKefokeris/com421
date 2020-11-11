

list = [20, 13, 17, 6, 1]
n = len(list)

#Outer Loop - iterations of algorithm
for i in range(n-1):   
    #inner loop - does the swapping
    for j in range(n-1-i): # For the first iteration i will be 0, so j will loop from 0 up to but not including n-1-0 i.e. 4(in this case)
        # For the second iteration i will be 1 so j will loop from 0 up to but not including n-1-1 (i.e. 3)
        if list[j] > list[j+1]: #wrong order
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp


print(list)

