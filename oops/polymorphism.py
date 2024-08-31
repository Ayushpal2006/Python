class Animal:
    def __init__(self,name):
        self.name = name
    
    def showName(self):
        print(self.name)
    
class Human(Animal):
    
    def showName(self):
        super().showName() 
        print("this from Human ::",self.name)
        
        
obj1 = Human("ayush")
obj1.showName()    