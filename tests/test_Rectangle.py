from src.Rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    ('side_a', 'side_b', 'area'),
    [
        pytest.param(3, 6, 18, id='area 1 = 18 (int)'),
        pytest.param(3.5, 5.5, 19.25, id='area 2 = 19.25 (float)'),
    ],
)
def test_rectangle_area_positive(side_a, side_b, area):
    rect_1 = Rectangle(side_a, side_b)
    assert rect_1.get_area == area


@pytest.mark.parametrize(
    ('side_a', 'side_b'),
    [
        pytest.param(-4, 3, id="отрицательное значение стороны"),
        pytest.param(4.4, 0, id="нулевое значение стороны")
    ],
)
def test_rectangle_negative_values(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
