class animal:
    
    def getdata(self):
        global ani 
        ani = input("Enter a animal name:- ")
        
    def showdata(self):
        print(f"Animal Name is:- {ani}")

while True:
    choi = int( input("Your want exit Enter 1\nContinuous Enter 2\n--------------------------------\n"))
    if choi == 1 :
        break
    else:
        a = animal
        a.getdata()
        a.showdata()
        print("-----------------------------")
        
    