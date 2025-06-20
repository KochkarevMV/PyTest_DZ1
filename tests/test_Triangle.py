from src.Triangle import Triangle
import pytest



@pytest.mark.parametrize(
    ('side_a', 'side_b', 'side_c', 'area'),
    [
        pytest.param(3, 5, 7, 6, id='площадь треугольника_1 = 6 (int)'),
    ],
)
def test_triangle_area_positive(side_a, side_b, side_c, area, enter_exit_points):
    tri_1 = Triangle(side_a, side_b, side_c)
    assert tri_1.get_area == area



@pytest.mark.parametrize(
    ('side_a', 'side_b', 'side_c', 'perimeter'),
    [
        pytest.param(2, 3, 4 , 9, id='периметр треугольника_1 = 9 (int)')
    ],
)
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    tri_2 = Triangle(side_a, side_b, side_c)
    assert tri_2.get_perimeter == perimeter



@pytest.mark.parametrize(
    ('side_a', 'side_b', 'side_c' ,'area_1', 'side_d', 'side_e', 'side_f', 'area_2'),
    [
      pytest.param(3, 5, 7, 6, 4, 3, 5, 6, id='сложение площадей 1 и 2 = 12'),
    ],
)
def test_triangle_add_area_positive(side_a, side_b, side_c, area_1, side_d, side_e, side_f, area_2):
    tri_3 = Triangle(side_a, side_b, side_c)
    tri_4 = Triangle(side_d, side_e, side_f)
    assert tri_3.add_area(tri_4)



@pytest.mark.parametrize(
    ('side_a', 'side_b', 'side_c'),
    [
        pytest.param(0, 0, 0, id='нулевое значение сторон'),
        pytest.param(2, 3, 5, id='сумма длин двух сторон не должна быть равна длине третьей'),
        pytest.param(2, 3, 8, id='cумма длин двух сторон треуголника не должна быть меньше длины третьей стороны'),
    ],
)
def test_triangle_negative_values(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)



@pytest.mark.parametrize(
    ('string_1', 'string_2', 'string_3', 'area_1', 'side_a', 'side_b', 'side_c', 'area_2'),
    [
        pytest.param("5" , "3", "4", 10, 3, 5, 7, 6, id='принимается не фигура. должная быть фигура'),
    ],
)
def test_triangle_add_area_negative(string_1, string_2, string_3, area_1, side_a, side_b, side_c, area_2):
    try:
        tri_5 = Triangle(side_a, side_b, side_c)
        tri_6 = Triangle(string_1, string_2, string_3)
        print(tri_5.add_area(tri_6))
    except TypeError:
        print("Должна приниматься фигура с тремя сторонами. Только числа")
