class CarFactory:
    def __init__(self, name, top_speed, price):
        self.name = name
        self.top_speed = top_speed
        self.price = price

    def showDetails(self):
        print(f"name: {self.name} , Top speed : {self.top_speed} , Price : {self.price}")

class CarFactory2(CarFactory):
    def __init__(self, name, top_speed, price,jet):
        super().__init__(name, top_speed, price)
        self.jet = jet

class Maruti(CarFactory2):        
    def __init__(self, name, top_speed, price, jet,isUniqe):
        super().__init__(name, top_speed, price, jet)
        self.isUniqe = isUniqe
        