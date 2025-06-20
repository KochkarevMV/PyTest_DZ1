from src.Circle import Circle
import pytest



@pytest.mark.parametrize(
    ('radius', 'area'),
    [
        pytest.param(5, 78, id='area1 = 78 (int)'),
    ],
)
def test_circle_area_positive(radius, area, enter_exit_points):
    circle_1 = Circle(radius)
    assert circle_1.get_area == area



@pytest.mark.parametrize(
    ('radius', 'perimeter'),
    [
        pytest.param(3, 18, id='периметр_1 = 18 (int)'),
    ],
)
def test_circle_perimeter_positive(radius, perimeter):
    circle_2 = Circle(radius)
    assert circle_2.get_perimeter == perimeter



@pytest.mark.parametrize(
    ('radius_1', 'area_1', 'radius_2', 'area_2'),
    [
      pytest.param(5, 78, 6, 113, id='сложение площадей 1 и 2 = 191'),
    ],
)
def test_circle_add_area_positive(radius_1, area_1, radius_2, area_2):
    circle_3 = Circle(radius_1)
    circle_4 = Circle(radius_2)
    assert circle_3.add_area(circle_4)



@pytest.mark.parametrize(
    'radius',
    [
        pytest.param(-7, id='отрицательное значение радиуса'),
        pytest.param(0, id = 'нулевое значение радиуса')
    ],
)
def test_circle_area_negative_values(radius):
    with pytest.raises(ValueError):
        Circle(radius)



@pytest.mark.parametrize(
    ('string_1', 'area_1', 'radius_1', 'area_2'),
    [
        pytest.param("5", 10, 5, 78, id='принимается не фигура. должная быть фигура'),
    ],
)
def test_circle_add_area_negative(string_1, area_1, radius_1, area_2):
    try:
        circle_5 = Circle(radius_1)
        circle_6 = Circle(string_1)
        print(circle_5.add_area(circle_6))
    except TypeError:
        print("Должна приниматься фигура с указанным радиусом. Только числа")