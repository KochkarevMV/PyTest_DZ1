import pytest

@pytest.fixture
def enter_exit_points():
    print("\nСтарт теста")
    yield
    print("\nКонец теста")


