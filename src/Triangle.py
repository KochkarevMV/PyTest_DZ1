from Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, tri_a, tri_b, tri_c):
        if tri_a <= 0 or tri_b <= 0 or tri_c <= 0:
            raise ValueError("Длина сторон должна быть больше нуля")
        if tri_a + tri_b == tri_c or tri_a + tri_c == tri_b or tri_b + tri_c == tri_a:
            raise ValueError("Сумма длин двух сторон треуголника не должна быть равна длине третьей стороны")
        if tri_a + tri_b < tri_c or tri_a + tri_c < tri_b or tri_b + tri_c < tri_a:
            raise ValueError("Сумма длин двух сторон треуголника не должна быть меньше длины третьей стороны")
        self.tri_a = tri_a
        self.tri_b = tri_b
        self.tri_c = tri_c

    @property
    def get_perimeter(self):
        return self.tri_a + self.tri_b + self.tri_c

    @property
    def get_area(self):
        tri_p = (self.tri_a + self.tri_b + self.tri_c)/2
        tri_s = math.trunc(math.sqrt(tri_p*(tri_p-self.tri_a)*(tri_p-self.tri_b)*(tri_p-self.tri_c)))
        return tri_s
