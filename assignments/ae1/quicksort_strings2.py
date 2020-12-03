import math

def hoare(data, start, end):
    i = start
    j = end
    mid = math.floor((start + end) / 2)
    pivot = data[mid]

    while True:

        while (data[i] < pivot):
            i += 1
        while (data[j] > pivot):
            j = j-1
        
        if i >= j:
            return j
        else:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
        

def quicksort(data, start, end):
    
    if end >= start:
        pivot = hoare(data, start, end)
        quicksort(data, start, pivot-1)
        quicksort(data, pivot+1, end)
    
    return data



if __name__ == "__main__":
    unsorted = [47,36,14,21,91,18,17,82,84,6,73]

    quicksort(unsorted,0,10)

    print(unsorted)
