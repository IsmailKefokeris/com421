import quicksort_strings2 as quicksort
from collections import deque

class Poi():
    def __init__(self):
        self.poi = {}
        self.enquire = {}
        is_running = True

        while (is_running):
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
                search = Poi.search(self,name)
                print(search)

            elif ("c" in action.lower()):
                Poi.display(self)
            elif ("d" in action.lower()):
                print ("")
                name = str(input("What is the name of the POI you are going to remove: "))
                search = Poi.search(self, name)
                Poi.delete(self, search[0])
            
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


    def search(self, name):
        count = 0
        temp = []
        for key in self.poi:
            if (name in key):
                entries = self.poi[key]
                count += 1
                temp.append([key, entries[3]])
        
        print ("We have found {} matching results together with their post codes".format(count))
        print ("")
        if count > 1:
            print (temp)
            name = str(input("Please re enter the correct name for the establishment you want...."))
            Poi.search(self, name)
            return [name, self.poi[name]]
        elif count == 1:
            print ("-------------------------------------------------")
            print ("Results: {}".format(self.poi[temp[0][0]]))
            print ("Would you like to make any enquiries on the selected establishment?")
            print ("[A] Yes")
            print ("[B] No")
            action = str(input(" :"))
            if (action.lower() == "a"):
                Poi.enquiries(self,temp[0][0],False)
                return self.poi[temp[0][0]]
            elif (action.lower() == "b"):
                return self.poi[temp[0][0]]
            else:
                print ("Sorry something went wrong...")
                return self.poi[temp[0][0]]
        else:
            print ("ERROR.....")
            print ("Item Not Found Try Again...")
            print ("")
            print ("-------------------------------------------------")
                
                
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