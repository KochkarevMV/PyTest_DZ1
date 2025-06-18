from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, circle_Radius):
        if circle_Radius <= 0:
            raise ValueError("Радиус круга должен быть больше нуля")
        self.circle_Radius = circle_Radius

    @property
    def get_perimeter(self):
        circle_Perimetr = math.trunc(2*math.pi*self.circle_Radius)
        return circle_Perimetr
    
    @property
    def get_area(self):
        circle_Area = math.trunc(math.pi*(self.circle_Radius**2))
        return circle_Area