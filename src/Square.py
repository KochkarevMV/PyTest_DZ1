from Figure import Figure
    

class Square(Figure):
    def __init__(self, square_side_a):
        if square_side_a <= 0:
            raise ValueError("Сторона квадрата должна быть больше нуля")
        self.square_side_a = square_side_a

    @property
    def get_perimeter(self):
        return self.square_side_a * 4
    
    @property
    def get_area(self):
        return self.square_side_a * self.square_side_a
