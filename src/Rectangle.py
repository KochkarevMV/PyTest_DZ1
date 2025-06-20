from Figure import Figure


class Rectangle(Figure):
    def __init__(self, rect_side_a, rect_side_b):
        if rect_side_a <= 0 or rect_side_b <= 0:
            raise ValueError("Сторона прямоугольника должна быть больше нуля")
        self.rect_side_a = rect_side_a
        self.rect_side_b = rect_side_b

    @property
    def get_perimeter(self):
        return (self.rect_side_a + self.rect_side_b) * 2
    
    @property
    def get_area(self):
        return self.rect_side_a * self.rect_side_b