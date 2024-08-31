from abc import Abc, abstractMethod

class Shape(Abc):
    @abstractMethod
    def area():
        pass
    
    @abstractMethod
    def perimeter():
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area():
        pass

    def perimeter():
        pass

circle = Circle(22)