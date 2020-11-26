import math

def split(data):
    letters = list(data)
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    index = alpha.index(letters[0])
    return index

def hoare(data, start, end):
    i = start
    j = end
    mid = math.floor((start + end) / 2)
    pivot = data[mid]
    
    
    while True:
        data1 = split(data[i])
        data2 = split(data[j])
        pivo = split(pivot)
        

        while (data1 < pivo):
            i += 1
            data1 = split(data[i])
        while (data2 > pivo):
            j = j-1
            data2 = split(data[j])
        
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
    



unsorted = [
    "ace",
    "chase",
    "base",
    "kace",
    "lase",
    "jase",
    "uce",
    "zase",
    "rhase",
    "pase",
    "oase"
    ]

quicksort(unsorted,0,10)

print(unsorted)
