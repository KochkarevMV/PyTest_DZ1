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
    ('radius', 'area'),
    [
        pytest.param(-7, -43, id='отрицательное значение радиуса'),
        pytest.param(0, 0, id = 'нулевое значение радиуса')
    ],
)
def test_circle_area_negative_values(radius, area):
    circle_3 = Circle(radius)
    with pytest.raises(ValueError):
        Circle(radius)
