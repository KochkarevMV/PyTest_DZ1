from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, circle_radius):
        if circle_radius <= 0:
            raise ValueError("Радиус круга должен быть больше нуля")
        self.circle_Radius = circle_radius

    @property
    def get_perimeter(self):
        circle_perimetr = math.trunc(2*math.pi*self.circle_Radius)
        return circle_perimetr
    
    @property
    def get_area(self):
        circle_area = math.trunc(math.pi*(self.circle_Radius**2))
        return circle_area
