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
    ('side_a', 'side_b', 'side_c', 'area'),
    [
        pytest.param(0, 0, 0, 0, id='нулевое значение сторон'),
        pytest.param(2, 3, 5, 5, id='сумма длин двух сторон не должна быть равна длине третьей'),
        pytest.param(2, 3, 8, 8, id='cумма длин двух сторон треуголника не должна быть меньше длины третьей стороны'),
    ],
)
def test_triangle_negative_values(side_a, side_b, side_c, area):
    tri_2 = Triangle(side_a, side_b, side_c)
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


