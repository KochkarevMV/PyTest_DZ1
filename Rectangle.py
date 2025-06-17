from Figure import Figure


class Rectangle(Figure):
    def __init__(self, Rect_Side_A, Rect_Side_B):
        if Rect_Side_A <= 0 or Rect_Side_B <= 0:
            raise ValueError("Сторона прямоугольника должна быть больше нуля")
        self.Rect_Side_A = Rect_Side_A
        self.Rect_Side_B = Rect_Side_B

    @property
    def get_perimeter(self):
        return (self.Rect_Side_A + self.Rect_Side_B) * 2
    
    @property
    def get_area(self):
        return self.Rect_Side_A * self.Rect_Side_B