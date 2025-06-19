from src.Square import Square
import pytest



@pytest.mark.parametrize(
    ('side_a', 'area'),
    [
        pytest.param(3, 9, id='area1 = 9 (int)'),
        pytest.param(3.4, 11.559999999999999, id='area2 = 11.56 (float)')
    ],
)
def test_square_area_positive(side_a, area, enter_exit_points):
    square_1 = Square(side_a)
    assert square_1.get_area == area



@pytest.mark.parametrize(
    ('side_a', 'perimeter'),
    [
        pytest.param(5, 20, id='периметр_1 = 20 (int)'),
        pytest.param(4.3, 17.2, id='периметр_2 = 17.2 (float)')
    ],
)
def test_square_perimeter_positive(side_a, perimeter):
    square_3 = Square(side_a)
    assert square_3.get_perimeter == perimeter



@pytest.mark.parametrize(
    ('side_a', 'area'),
    [
        pytest.param(-7, -49, id='отрицательное значение стороны'),
        pytest.param(0, 0, id = 'нулевое значение стороны')
    ],
)
def test_square_area_negative_values(side_a, area):
    square2 = Square(side_a)
    with pytest.raises(ValueError):
        Square(side_a)
