from Figure import Figure
    

class Square(Figure):
    def __init__(self, square_side_A):
        if square_side_A <= 0:
            raise ValueError("Сторона квадрата должна быть больше нуля")
        self.square_side_A = square_side_A

    @property
    def get_perimeter(self):
        return self.square_side_A * 4
    
    @property
    def get_area(self):
        return self.square_side_A*self.square_side_A