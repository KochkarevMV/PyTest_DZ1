from src.Rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    ('side_a', 'side_b', 'area'),
    [
        pytest.param(3, 6, 18, id='area 1 = 18 (int)'),
        pytest.param(3.5, 5.5, 19.25, id='area 2 = 19.25 (float)'),
    ],
)
def test_rectangle_area_positive(side_a, side_b, area, enter_exit_points):
    rect_1 = Rectangle(side_a, side_b)
    assert rect_1.get_area == area



@pytest.mark.parametrize(
    ('side_a', 'side_b', 'perimeter'),
    [
        pytest.param(3, 4, 14, id='perimetr_1 = 14 (int)'),
        pytest.param(2.5, 6.4, 17.8, id='perimetr_2 = 17.8 (int)')
    ],
)
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    rect_2 = Rectangle(side_a, side_b)
    assert rect_2.get_perimeter == perimeter



@pytest.mark.parametrize(
    ('side_a', 'side_b', 'area_1', 'side_c', 'side_d', 'area_2'),
    [
      pytest.param(3, 6, 18, 5, 7, 35, id='сложение площадей 1 и 2 = 53'),
    ],
)
def test_rectangle_add_area_positive(side_a, side_b, area_1, side_c, side_d, area_2):
    rect_3 = Rectangle(side_a, side_b)
    rect_4 = Rectangle(side_c, side_d)
    assert rect_3.add_area(rect_4)



@pytest.mark.parametrize(
    ('side_a', 'side_b'),
    [
        pytest.param(-4, -3, id="отрицательное значение стороны"),
        pytest.param(0, 0, id="нулевое значение стороны")
    ],
)
def test_rectangle_negative_values(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)



@pytest.mark.parametrize(
    ('string_1', 'string_2', 'area_1', 'side_a', 'side_b', 'area_2'),
    [
        pytest.param("5" , "3", 10, 3, 6, 18, id='принимается не фигура. должная быть фигура'),
    ],
)
def test_rectangle_add_area_negative(string_1, string_2, area_1, side_a, side_b, area_2):
    try:
        rect_5 = Rectangle(side_a, side_b)
        rect_6 = Rectangle(string_1, string_2)
        print(rect_5.add_area(rect_6))
    except TypeError:
        print("Должна приниматься фигура с двумя сторонами. Только числа")
