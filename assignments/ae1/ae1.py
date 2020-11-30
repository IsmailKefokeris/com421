import quicksort_strings2 as quicksort

class poi():
    def __init__(self):
        self.poi = {}
        is_running = True

        while (is_running):
            print ("-------------------------------------------------")
            print ("What would you like to do today?: ")
            print ("[A] Add a new POI")
            print ("[B] Search for a specific POI")
            print ("[C] List all POI")
            print ("[D] Delete a specific POI")
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
                        poi.add(self,name,establishment,description,address)
                        running = False
                    elif ("b" in action.lower()):
                        print ("Resetting.....")
                        print ("-------------------------------------------------")

            elif ("b" in action.lower()):
                print ("")
                name = str(input("What is the name of the POI: "))
                search = poi.search(self,name)
                print(search[1])

            elif ("c" in action.lower()):
                poi.display(self)
            elif ("d" in action.lower()):
                print ("")
                name = str(input("What is the name of the POI you are going to remove: "))
                search = poi.search(self, name)
                poi.delete(self, search[0])

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
            poi.search(self, name)
            return [name, self.poi[name]]
        elif count == 1:
            return self.poi[name]
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
            poi.search(self,action)

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





def run():
    poi()

run()