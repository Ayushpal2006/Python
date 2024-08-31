class CarFactory:
    def __init__(self, name, top_speed, price):
        self.name = name
        self.top_speed = top_speed
        self.price = price

    def showDetails(self):
        print(f"name: {self.name} , Top speed : {self.top_speed} , Price : {self.price}")

class Maruti(CarFactory):        
    def __init__(self, name, top_speed, price , isUniqe):
        super().__init__(name, top_speed, price)
        self.isUniqe = isUniqe
        
        
obj1 = Maruti(1,2,3,True)
print(obj1.isUniqe)

obj1.showDetails()

# Ferrari = CarFactory("Ferrari", 250, "2 cr")

# Ferrari.showDetails()