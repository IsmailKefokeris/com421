

class hashtable():

    def __init__(self):
        self.table = [None] * 10 
        
    def put(self, key, value):
        hashcode = 0
        count = 0

        for char in key:
            hashcode += ord(char) * (31**count)
            count += 1

        pos = hashcode % 10
        
        if self.table[pos] is None:
            self.table[pos] = []
        else:
            if (pos > len(self.table)-1):
                pos = 0
                while self.table[pos] is not None:
                    pos += 1
                    if (pos > len(self.table)-1):
                        return ("ERROR HASH TABLE FULL")
                self.table[pos] = []
            else:
                while self.table[pos] is not None:
                    pos += 1
                    if (pos > len(self.table)-1):
                        pos = 0
                        while self.table[pos] is not None:
                            pos += 1
                            if (pos > len(self.table)-1):
                                return ("ERROR HASH TABLE FULL")
                self.table[pos] = []
                
        self.table[pos].append((key,value))   

    def get(self, key):
        hashcode = 0
        count = 0
        count2 = 0

        for char in key:
            hashcode += ord(char) * (31**count)
            count += 1

        pos = hashcode % 10

        if self.table[pos] is None:
            return ("ERROR Nothing stored with the key: {}".format(key))
        else:
            while count2 != len(self.table[pos]):

                if key == self.table[pos[count2][0]]:
                    print(self.table[pos[count2][0]])
                    print(self.table[pos[count2][1]])

                count2 += 1        

    def __str__(self):
        return self.table.__str__()

table = hashtable()

table.put("cat", "A Furry Animal which goes boomies")

table.put("act", "skawies animools")