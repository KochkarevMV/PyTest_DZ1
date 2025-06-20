from Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, tri_A, tri_B, tri_C):
        if tri_A <= 0 or tri_B <= 0 or tri_C <= 0:
            raise ValueError("Длина сторон должна быть больше нуля")
        if tri_A + tri_B == tri_C or tri_A + tri_C == tri_B or tri_B + tri_C == tri_A:
            raise ValueError("Сумма длин двух сторон треуголника не должна быть равна длине третьей стороны")
        if tri_A + tri_B < tri_C or tri_A + tri_C < tri_B or tri_B + tri_C < tri_A:
            raise ValueError("Сумма длин двух сторон треуголника не должна быть меньше длины третьей стороны")
        self.tri_A = tri_A
        self.tri_B = tri_B
        self.tri_C = tri_C

    @property
    def get_perimeter(self):
        return self.tri_A + self.tri_B + self.tri_C

    @property
    def get_area(self):
        tri_p = (self.tri_A + self.tri_B + self.tri_C)/2
        tri_s = math.trunc(math.sqrt(tri_p*(tri_p-self.tri_A)*(tri_p-self.tri_B)*(tri_p-self.tri_C)))
        return tri_s
