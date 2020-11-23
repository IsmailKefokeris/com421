class poi():
    def __init__(self):
        self.poi = {}
        is_running = True

        while (is_running):
            print ("What would you like to do today?: ")
            print ("[A] Add a new POI")
            print ("[B] Search for a specific POI")
            print ("[C] List all POI")
            print ("[D] Delete a specific POI")
            print ("[Q] Quit....")

            action = input()

            if ("a" in action.lower()):
                print ("")
                name = str(input("What is the name of this POI: "))
                establishment = str(input("What type of establishment is it: "))
                description = str(input("Give me a short description: "))
                address = str(input("What is the address: "))

                poi.add(self,name,establishment,description,address)

            elif ("b" in action.lower()):
                print ("")
                name = str(input("What is the name of the POI: "))
                poi.search(self,name)

            elif ("c" in action.lower()):
                pass
            elif ("d" in action.lower()):
                pass
            elif ("q" in action.lower()):
                print ("")
                print ("Quitting.....")
                break


    
    def add(self, name, establishment, description, address):
        
        count = 0
        for key in self.poi:
            count += 1
            if (name in key):
                name = name + str(count)
        
        self.poi[name] = [name, establishment, description, address]


    def search(self, name):
        pass

    def display(self):
        pass



def run():
    poi()

run()