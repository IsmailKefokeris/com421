
class selection_sort():

    def __init__(self, list):
        self.unsorted = list

    def sort(self):
        sorted = []
        unsortedindex = len(self.unsorted)
        v = 0
        swapn = False
        for index in range(unsortedindex+v):
                curmin = self.unsorted[index]
                for i2 in range(unsortedindex+v):
                    nextvalue = self.unsorted[i2]
    
                    if nextvalue < curmin:
                        
                        if i2 != 0:
                            curmin = nextvalue
                            swapn = True
                        else:
                            curmin = nextvalue
                            
                    
                if swapn == True:
                    temp = self.unsorted[i2]
                    
                    self.unsorted[i2] = self.unsorted[index]
                    self.unsorted[index] = temp
                    del self.unsorted[index]
                    v += -1
                    sorted.append(curmin)
                    swapn = False
                else:    
                    del self.unsorted[index+v]
                    v += -1
                    sorted.append(curmin)            



    def display(self):
        pass
    

list = selection_sort([5,2,6,9,1])

list.sort()