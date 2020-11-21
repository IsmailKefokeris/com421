def binarysearch(list,high,low,item):

    while (low <= high):
        mid = int((low + high) / 2)

        if list[mid] == item:
            return mid
        
        elif list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

data = [i*i for i in range(1,100)]

result = binarysearch(data,99,0,81)

if result != -1:
    print("Your item was at index {}".format(result))
else:
    print("NOT AVAILABLE IN LIST")