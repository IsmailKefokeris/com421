import quicksort_strings2 as quicksort
from collections import deque
from binary_search_exercise1 import binarysearch

class Poi():
    def __init__(self):
        self.poi = {}
        self.enquire = {}

        while True:
            print ("-------------------------------------------------")
            print ("What would you like to do today?: ")
            print ("[A] Add a new POI")
            print ("[B] Search for a specific POI")
            print ("[C] List all POI")
            print ("[D] Delete a specific POI")
            print ("[E] *Employee Only* Answer Enquiries")
            print ("[Q] Quit....")
            print ("-------------------------------------------------")

            action = input()

            if ("a" in action.lower()):
                running = True
                while (running):
                    print ("")
                    name = str(input("What is the name of this POI: "))
                    establishment = str(input("What type of establishment is it: "))
                    description = str(input("Give me a short description: "))
                    address = str(input("What is the post-code: "))
                    print ("-------------------------------------------------")
                    print ("Are you happy with the values entered?")
                    print ("[A] Yes")
                    print ("[B] No")
                    action = str(input())

                    if ("a" in action.lower()):
                        Poi.add(self,name,establishment,description,address)
                        running = False
                    elif ("b" in action.lower()):
                        print ("Resetting.....")
                        print ("-------------------------------------------------")

            elif ("b" in action.lower()):
                print ("")
                name = str(input("What is the name of the POI: "))
                Poi.search(self,name)

            elif ("c" in action.lower()):
                Poi.display(self)
            elif ("d" in action.lower()):
                print ("")
                name = str(input("What is the name of the POI you are going to remove: "))
                search = Poi.search(self, name)
                Poi.delete(self, search)
            
            elif ("e" in action.lower()):
                stored_pois = []
                for key in self.poi.keys():
                    stored_pois.append(key)
                    stored_pois.append(self.poi[key][3])
                print ("-------------------------------------------------")    
                print (stored_pois)
                print ("This is the list of saved establishments and post-codes, Type out the name of the establishment you would like to view")
                action = input(" :")
                self.enquiries(action,True)

            elif ("q" in action.lower()):
                print ("")
                print ("Quitting.....")
                break

    
    def add(self, name, establishment, description, address):
        actual_key = name
        count = 0
        edit = False
        for key in self.poi:
            count += 1
            if (actual_key in key):
                edit = True
                actual_key = actual_key + str(count)

        if(edit is False):
            actual_key = actual_key + str(count)
        
        self.poi[actual_key] = [name, establishment, description, address]


    def specific_search(self, name):
        empty_list = []

        for key in self.poi:
            empty_list.append(key)

        end = len(empty_list) - 1
        start = end - end
        quicksort.quicksort(empty_list, start, end)
        result = binarysearch(empty_list,end,start,name)

        if result != -1:
            print (f"Values from {empty_list[result]}")
            print(self.poi[empty_list[result]])
            return empty_list[result]
        else:
            print("Name Either Incorrect or doesnt Exist....")

                
                
    def display(self):
        empty_list = []

        for key in self.poi:
            empty_list.append(key)

        end = len(empty_list) - 1
        start = end - end
        quicksort.quicksort(empty_list, start, end)
        print (empty_list)
        print ("-------------------------------------------------")
        print ("Would you like to select a POI?")
        print ("[A] Yes")
        print ("[B] No")
        print ("-------------------------------------------------")
        action = str(input())

        if ("a" in action.lower()):
            print ("-------------------------------------------------")
            action = str(input("Enter the name of the POI: "))
            Poi.search(self,action)

        elif ("b" in action.lower()):
            print ("Going back to main menu.....")
            print ("-------------------------------------------------")
    
    def delete(self, name):
        print("Are you sure you want to delete the POI: {}?".format(name))
        print ("[A] Yes")
        print ("[B] No")
        print ("-------------------------------------------------")
        action = str(input(" : "))

        if ("a" in action):
            del self.poi[name]
        else:
            print ("Returning to Main menu.....")
            print ("")
            print ("")

    def enquiries(self,name,employee):
        employee = employee
        
        if (employee is False):
            print ("What would you like to ask?")
            question = input(" :")

            if (name in self.enquire):
                print ("-------------------------------------------------")
                print ("Saving Question....")
                print (" ")
                self.enquire[name].append(question)
            else:
                self.enquire[name] = deque()
                self.enquire[name].append(question)
        else:
            while True:
                try:
                    question = self.enquire[name].popleft()
                    print (question)
                    _ = input("Enter your answer here: ")
                    print ("-------------------------------------------------")
                    print ("Thank you for your response....")
                    print ("-------------------------------------------------")
                    return
                except:
                    print ("No Questions Available..")
                    return


def run():
    Poi()

run()