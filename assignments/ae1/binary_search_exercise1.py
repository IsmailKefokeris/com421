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

if __name__ == "__main__":
    data = ["a","b","c","d","e","f","g"]
    

    result = binarysearch(data,6,0,"e")

    if result != -1:
        print("Your item was at index {}".format(result))
    else:
        print("NOT AVAILABLE IN LIST")