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
    square_2 = Square(side_a)
    assert square_2.get_perimeter == perimeter



@pytest.mark.parametrize(
    ('side_1', 'area_1', 'side_2', 'area_2'),
    [
      pytest.param(3, 9, 4, 16, id='сложение площадей 1 и 2 = 25'),
    ],
)
def test_square_add_area_positive(side_1, area_1, side_2, area_2):
    square_3 = Square(side_1)
    square_4 = Square(side_2)
    assert square_3.add_area(square_4)



@pytest.mark.parametrize(
    'side_a',
    [
        pytest.param(-7, id='отрицательное значение стороны'),
        pytest.param(0, id = 'нулевое значение стороны')
    ],
)
def test_square_area_negative_values(side_a):
    with pytest.raises(ValueError):
        Square(side_a)



@pytest.mark.parametrize(
    ('string_1', 'area_1', 'side_a', 'area_2'),
    [
        pytest.param("5" , 10, 3, 9, id='принимается не фигура. должная быть фигура'),
    ],
)
def test_square_add_area_negative(string_1, area_1, side_a, area_2):
    try:
        square_5 = Square(side_a)
        square_6 = Square(string_1)
        print(square_5.add_area(square_6))
    except TypeError:
        print("Должна приниматься фигура с одной стороной. Только числа")