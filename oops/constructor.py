class CarFactory:
    def __init__(self, name, top_speed, price):
        self.name = name
        self.top_speed = top_speed
        self.price = price

    def showDetails(self):
        print(f"name: {self.name} , Top speed : {self.top_speed} , Price : {self.price}")
        
        
Ferrari = CarFactory("Ferrari", 250, "2 cr")

Ferrari.showDetails()